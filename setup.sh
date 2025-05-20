#!/bin/bash

# .envファイルが既に存在するかチェック
if [ -f .env ]; then
    echo ".envファイルが既に存在します。上書きしますか？ (y/n)"
    read answer
    if [ "$answer" != "y" ]; then
        echo "セットアップをキャンセルしました。"
        exit 0
    fi
fi

# Last.fmのAPIキーを入力してもらう
echo "Last.fmのAPIキーを入力してください（https://www.last.fm/api から取得できます）:"
read api_key

# .envファイルを作成
cat > .env << EOL
LASTFM_API_KEY=${api_key}
EOL

echo ".envファイルの作成が完了しました！"
echo "これでdevcontainerを起動できます。" 