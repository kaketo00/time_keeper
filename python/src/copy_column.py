import mysql.connector
import os
from dotenv import load_dotenv
import datetime
import schedule
import time

# 起動時間
h = 18
m = "37"
H = h - 9
looptime = "%02d:%s" % (H, m)

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

def job():
    try:
        connection = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASS,
        database = DB_NAME
        )

        cursor = connection.cursor()

        # ここにループ内容を記述
        # テーブルのコピー
        enter_day = datetime.datetime.now().strftime("%Y-%m-%d")
        sql1 = '''
        INSERT INTO entertimes_day (
        user_id,
        user_name,
        user_staytime,
        user_guild_id,
        enter_day
        )
        SELECT
        user_id,
        user_name,
        user_staytime,
        user_guild_id,
        %s
        FROM users
        '''
        cursor.execute(sql1, (enter_day,))

        # 元テーブルの内容をリセット
        sql2 = '''
        truncate table users
        '''
        cursor.execute(sql2)

    finally:
        if connection is not None and connection.is_connected():
            connection.close()

schedule.every().day.at(looptime).do(job)
  
while True:
    schedule.run_pending()
    time.sleep(60)
