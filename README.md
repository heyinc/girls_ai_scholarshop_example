# K-POP 人気曲ランキング Webアプリ

このリポジトリは、K-POPの人気曲ランキングをWeb上で簡単に閲覧・分析できるアプリケーションです。ユーザーは期間や表示件数、優遇したいアーティストや係数を自由に選択し、ランキングをカスタマイズできます。

## 主な技術とその解説
- **Python**: アプリケーションの主要なロジックを記述するプログラミング言語。
- **Streamlit**: Python製のWebアプリケーションフレームワーク。データ可視化やインタラクティブなUIを簡単に作成できます。
- **Pandas**: データの集計・加工・分析を行うためのPythonライブラリ。
- **Last.fm API**: K-POPの人気曲データを取得するための外部API。
- **devcontainer（開発コンテナ）**: Dockerを利用した、誰でも同じ開発環境をすぐに用意できる仕組み。
- **Cursor/VS Code**: devcontainer対応のエディタ。開発環境の起動やコード編集に利用します。

---

## devcontainerとは？

devcontainer（開発コンテナ）とは、開発に必要なツールやライブラリ、設定があらかじめ用意された「開発専用の仮想環境」です。プロジェクトごとに最適な環境をすぐに用意できるため、

- 「環境構築でつまずかない」
- 「誰でも同じ環境で開発できる」
- 「ローカルPCを汚さずに開発できる」

といったメリットがあります。

このリポジトリでは、devcontainerを使うことで、Pythonや必要なパッケージ、設定済みの環境で簡単にアプリを動かすことができます。

## devcontainerの起動方法（必ずこの手順が必要です！）

1. Dockerをインストールしてください。
2. CursorやVS Codeなど、devcontainer対応エディタでこのリポジトリを開きます。
3. **必ず「Reopen in Container」や「Open in devcontainer」などの操作を行ってください。これをしないと開発環境が正しく立ち上がりません。**

> **Cursorの場合**
> 
> ターミナルでプロジェクトのディレクトリに移動し、
> 
> ```bash
> cursor .
> ```
> 
> と入力してください。エディタが開いた後、画面上部や左下に「Reopen in Container」ボタンが表示された場合は必ずクリックしてください。
>
> **VS Codeの場合**
> 
> 「Remote-Containers」拡張機能をインストールし、画面左下の「><」マークやコマンドパレットから「Reopen in Container」を選択してください。

> ⚠️ devcontainerを起動しないと、必要なツールやライブラリが使えず、アプリが正しく動作しません。

---

## 使い方

### 1. 必要なもの
- Docker（https://www.docker.com/ja-jp/get-started/）
- Cursor（https://www.cursor.com/）または VS Code（https://code.visualstudio.com/）
- Last.fm APIキー（https://www.last.fm/api/account/create で取得）

### 2. リポジトリをクローン
```bash
git clone https://github.com/stores-girls-ai-scholarship/stores-girls-ai-scholarship-example.git
cd stores-girls-ai-scholarship-example
```

### 3. セットアップ（.envファイルの自動作成）
`./setup.sh` を実行すると、Last.fmのAPIキーを入力するだけで `.env` ファイルが自動で作成されます。

```bash
./setup.sh
```

> すでに .env ファイルが存在する場合は、上書きするかどうか確認されます。

### 4. 開発環境（devcontainer）の起動
```bash
cursor .
```
または VS Code の「Reopen in Container」などでdevcontainerを起動してください。

### 5. Streamlitアプリの起動（必ずdevcontainer内で実行）
開発環境（devcontainerやターミナル）内で、以下のコマンドを実行してください。

```bash
streamlit run app.py
```

> ⚠️ このコマンドは必ずdevcontainer内で実行してください。ローカルPCのターミナルで直接実行しても正しく動作しません。

起動後、表示されるURL（通常は http://localhost:8501 など）にブラウザでアクセスしてください。

### 6. Webアプリの使い方
1. 期間・表示件数・優遇アーティスト・係数を選択すると、K-POP人気曲ランキングが表示されます。
2. 表示件数や優遇アーティストは画面上で自由に変更できます。

---

## FAQ・トラブルシューティング

**Q. devcontainerがうまく起動しません**  
A. Dockerが起動しているか、Cursor/VS Codeの拡張機能が正しくインストールされているか確認してください。

**Q. .envファイルが見つからない/エラーになる**  
A. 必ず `./setup.sh` を実行し、APIキーを入力してください。

**Q. Streamlitアプリが起動しない/エラーが出る**  
A. 必ずdevcontainer内のターミナルで `streamlit run app.py` を実行してください。

**Q. APIキーが正しいのにデータが取得できない**  
A. Last.fmのAPI利用制限や、APIキーの入力ミスがないかご確認ください。

---

何か問題があれば、[Last.fm APIキーの取得方法](https://www.last.fm/api/account/create)や、Docker/Cursor/VS Codeの公式ドキュメントもご参照ください。