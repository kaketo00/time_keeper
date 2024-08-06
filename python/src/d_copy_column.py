from discord.ext import commands, tasks
from os import getenv, name
import discord
import datetime
import zoneinfo
import mysql.connector
import os
from dotenv import load_dotenv

connection = None

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

# 後で権限変更
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# 時刻変更（変数の変更も忘れずに）
# utc = datetime.timezone.utc
jst = zoneinfo.ZoneInfo(key='Asia/Tokyo')

# ループ時刻変更（カラム追加は日付変更の若干前におこなっておく）
# times = [
#     datetime.time(hour=16, minute=40, second=30, tzinfo=jst)
# ]
times = [
    datetime.time(second=30, tzinfo=jst)
]

day = datetime.day(tzinfo=jst)

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=times)
    async def my_task(self):
        print("a")
        print(day)
        connection = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            password = DB_PASS,
            database = DB_NAME
        )
        cursor = connection.cursor()
        # ここにループ内容を記述
        # テーブルのコピー
        sql1 = '''
        INSERT INTO entertimes_day (
        user_id,
        user_name,
        user_staytime,
        user_guild_id
        )
        SELECT user_id,
        user_name,
        user_staytime,
        user_guild_id
        FROM users
        '''
        cursor.execute(sql1)

        # 日付カラムに内容を追加
        sql3 = '''
        INSERT INTO entertimes_day (
        enter_day
        )
        VALUES (%s)
        ''',( str(time.time()))
        cursor.execute(sql3)
        # 元テーブルの内容をリセット
        sql3 = ''''''
        cursor.execute(sql3)