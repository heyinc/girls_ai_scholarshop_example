import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import os

# Last.fm APIの設定
API_KEY = os.getenv("LASTFM_API_KEY")
BASE_URL = "http://ws.audioscrobbler.com/2.0/"

# タイトルを表示
st.title('K-POP 人気曲ランキング')

# 期間を選択
period = st.selectbox(
    "期間を選択してください",
    ["7日間", "1ヶ月", "3ヶ月", "6ヶ月", "12ヶ月", "全体"]
)

# 表示件数を選択
display_limit = st.selectbox(
    "表示件数を選択してください",
    [50, 100, 200, 500, 1000],
    index=1,  # デフォルトで100件を選択
    help="表示する曲の数を選択できます。"
)

# 期間のマッピング
period_map = {
    "7日間": "7day",
    "1ヶ月": "1month",
    "3ヶ月": "3month",
    "6ヶ月": "6month",
    "12ヶ月": "12month",
    "全体": "overall"
}


def get_top_tracks(period, total_limit=1000):
    all_tracks = []
    per_page = 100  # Last.fmのAPIの最大limit
    for page in range(1, (total_limit // per_page) + 2):
        params = {
            "method": "tag.gettoptracks",
            "tag": "k-pop",
            "api_key": API_KEY,
            "format": "json",
            "period": period_map[period],
            "limit": per_page,
            "page": page
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if "tracks" in data and "track" in data["tracks"]:
            tracks = data["tracks"]["track"]
            all_tracks.extend(tracks)
            if len(tracks) < per_page:
                break  # これ以上データがない場合は終了
        else:
            break
        if len(all_tracks) >= total_limit:
            break
    return all_tracks[:total_limit]


def calc_rank(i, track, multiplier=100):
    """
    選択されたアーティストの曲の順位を上げる（1/multiplierにする）
    ただし、最小値は1とする
    """
    artist = track.get("artist", {}).get("name", "").lower()
    if artist.lower() in [a.lower() for a in favorite_artists]:
        return max(1, int((i + 1) / multiplier))
    else:
        return i + 1


if __name__ == "__main__":
    tracks = get_top_tracks(period, total_limit=2000)

    if tracks:
        # まず全データのDataFrameを作成
        df = pd.DataFrame([{
            "順位": i + 1,
            "曲名": track.get("name", "不明"),
            "アーティスト": track.get("artist", {}).get("name", "不明")
        } for i, track in enumerate(tracks)])

        # アーティストの一覧を取得
        available_artists = sorted(df["アーティスト"].unique())

        # 優遇するアーティストを選択
        favorite_artists = st.multiselect(
            "優遇するアーティストを選択してください（複数選択可）",
            available_artists,
            help="選択したアーティストの曲の順位が上がります"
        )

        # 順位調整係数を設定
        multiplier = st.slider(
            "優遇アーティストの順位調整係数（小さいほど上位に表示）",
            min_value=1,
            max_value=1000,
            value=100,
            step=1,
            help="優遇アーティストの曲の順位をこの値で割ります。値が小さいほど上位に表示されます。"
        )

        # 順位を再計算
        df["順位"] = df.apply(lambda row: calc_rank(
            row.name, {"artist": {"name": row["アーティスト"]}}, multiplier), axis=1)

        # 順位でソート
        df = df.sort_values("順位")
        # 選択された表示件数で制限
        df = df.head(display_limit)
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.error("データの取得に失敗しました。APIキーが正しく設定されているか、Last.fmの仕様が変わっていないかご確認ください。")
