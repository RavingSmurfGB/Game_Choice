FROM python:3.11-slim

RUN mkdir /app

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY discord_bot.py /app/discord_bot.py

CMD ["python3", "discord_bot.py"]