# ディスコートのボイスチャンネル滞在時間を計測するbotです

# 開発環境構築
`docker-compose build`

# 開発環境スタート
`docker-compose up`

# bot起動操作
1. `cd python/src`に移動
1. `python3 make_table.py`でテーブルの作成
1. `python3 discordbot.py`でbotの起動
1. `python3 copy_column.py`でデータを記録用カラムにコピー

# 開発環境ストップ
`docker-compose stop`
