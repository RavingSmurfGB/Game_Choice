# Game Choice

A small discord bot that selects a random game for us to play

## Requirements
There is only one environment variable required
- DISCORD_TOKEN: str, used to authenticate the bot with discord

## How to use

1. Create a discord bot: https://discord.com/developers/
2. under the bot section grab the discord token
3. build the docker image

```bash
sudo docker build -t discord_bot .
```

4. Run the docker image passing in the discord token from your created website
```bash
sudo docker run -d --restart=always --name discord_bot -e DISCORD_TOKEN="TOKEN HERE" discord_bot
```