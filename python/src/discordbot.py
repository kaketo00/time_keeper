# from discord.ext import commands
# from os import getenv, name
import discord
import time
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

# 後で権限変更
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_voice_state_update(member , before ,after):
    if before.channel != after.channel:
        if after.channel is not None:
            conn = mysql.connector.connect(
                host = DB_HOST,
                user = DB_USER,
                password = DB_PASS,
                database = DB_NAME
            )
            cur = conn.cursor()
            cur.execute("select * from users where user_id = %s",(member.id, ))
            rows = cur.fetchall()
            if not rows:
                cur.execute("INSERT INTO users VALUES (%s, %s ,%s ,%s)",(member.id, member.name,"0",member.guild.id ))
                conn.commit()
                print("new user recorded,He/She is " + member.name)
            cur.execute("INSERT INTO user_entertimes VALUES (%s, %s)",(member.id, str(time.time())))
            conn.commit()
            conn.close()

        if before.channel is not None:
            conn = mysql.connector.connect(
                host = DB_HOST,
                user = DB_USER,
                password = DB_PASS,
                database = DB_NAME
            )
            cur = conn.cursor()
            cur.execute("select * from user_entertimes where user_id = %s",(member.id, ))
            rows = cur.fetchall()
            enter_time = rows[0][1]
            print(enter_time)
            cur.execute("select * from users where user_id = %s",(member.id, ))
            staytime_rows = cur.fetchall()
            stay_time = staytime_rows[0][2]
            delta_stay_time = float(time.time()) - float(enter_time) + float(stay_time)
            cur.execute("UPDATE users SET user_staytime = %s WHERE user_id = %s AND user_guild_id = %s",(str(delta_stay_time),member.id,member.guild.id ))
            cur.execute("DELETE FROM user_entertimes WHERE user_id = %s",(member.id, ))
            conn.commit()
            conn.close()

token = os.getenv("DISCORD_BOT_TOKEN")
client.run(token)
