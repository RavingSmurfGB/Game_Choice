"""simple discord bot to choose a random game"""
import os
import random
import requests
import yaml

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

GAMES_LIST="https://raw.githubusercontent.com/RavingSmurfGB/Game_Choice/main/games_list.yaml"
RANDOM_PHRASE= [
    "Loki, the god of mischief has chosen: ",
    "I span the wheel and it came back with: ",
    "I've not rigged this but your game is: ",
    "Did you know you don't get taxed on your: ",
    "It was between WatchTogether and this, I thought you'd prefer this: ",
    "Fear Not! I'll save you and your boredom: " 
]

def get_games_list():
    """function to pull down current games list from main branch
    """
    games_request = requests.get(url=GAMES_LIST, timeout=60)
    if games_request.ok:
        return yaml.safe_load(games_request.text)

    return None

def filesize(size_gb: int):
    """Function to convert int into human readble strings
    """
    if size_gb < 1:
        size = f"{size_gb*100}MB"
    else:
        size = f"{size_gb}GB"
    return size

@bot.command(name="spin")
async def random_game(ctx):
    """Randomly chooses a game from the list
    """
    game = random.choice(get_games_list()['games'])
    phrase = random.choice(RANDOM_PHRASE)

    message = phrase + f"{game['game']} \nLink: {game['link']} \nFilesize: {filesize(game['size_gb'])}"

    await ctx.send(message)

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
