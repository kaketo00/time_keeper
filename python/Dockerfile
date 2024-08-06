FROM python:3.9.10-slim-buster

RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install mysql-connector-python
RUN pip3 install discord.py
RUN pip3 install python-dotenv
RUN pip install schedule

COPY ./python/src/ /app/

WORKDIR /app

# ここにDocker起動時に起動するpythonファイルを書く(テーブルを作ったりする)
# CMD python ./make_table.py
# CMD python ./discordbot.py

# make_table.py -> discordbot.py の順で実行する。
# python3 make_table.py　python3 discordbot.py
