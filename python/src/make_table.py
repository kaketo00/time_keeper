import mysql.connector
from os import getenv, name
import os
from dotenv import load_dotenv

connection = None

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

try:

    connection = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        passwd = DB_PASS,
        db = DB_NAME)
    cursor = connection.cursor()
    sql1 = '''
        CREATE TABLE users (
        user_id BIGINT NOT NULL PRIMARY KEY,
        user_name VARCHAR(50) NULL,
        user_staytime VARCHAR(50) NULL,
        user_guild_id VARCHAR(50) NULL
        )
        '''
    cursor.execute(sql1)

    sql2 = '''
        CREATE TABLE user_entertimes (
        user_id BIGINT NOT NULL PRIMARY KEY,
        user_entertime VARCHAR(50) NULL
        )
        '''
    cursor.execute(sql2)

    # 日付を０にしておく
    sql3 = '''
        CREATE TABLE entertimes_day (
        number int AUTO_INCREMENT PRIMARY KEY,
        user_id BIGINT NOT NULL DEFAULT 0,
        user_name VARCHAR(50) NULL DEFAULT 'Unknown',
        user_staytime VARCHAR(50) NULL DEFAULT 'Not specified',
        user_guild_id VARCHAR(50) NULL DEFAULT 'Not specified',
        enter_day VARCHAR(50) NULL DEFAULT 'Not specified'
        )
        '''
    cursor.execute(sql3)

    cursor.execute("SHOW TABLES")
    print(cursor.fetchall())

    cursor.close()

except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    if connection is not None and connection.is_connected():
        connection.close()