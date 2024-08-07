# ディスコートのボイスチャンネル滞在時間を計測するbotです

# 開発環境構築
`.env`の内容を更新  
`docker-compose build`

# 開発環境スタート
`docker-compose up`

# bot起動操作
1. `cd python/src`でディレクトリ移動
1. `python3 make_table.py`でテーブルの作成
1. `python3 discordbot.py`でbotの起動
1. `python3 copy_column.py`でデータを記録用カラムにコピー

# SQL操作
1. `cd mysql`でディレクトリ移動
2. `mysql -u ユーザー名 -p`でサーバーに接続
3. `use データベース名;`でデータベースの選択
4. `show tables;`でテーブル一覧の表示
5.  `select * from テーブル名;`でテーブルに格納されているデータの確認

# 開発環境ストップ
`docker-compose stop`
