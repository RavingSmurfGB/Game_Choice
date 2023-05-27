"""simple discord bot to choose a random game"""
import os
import random
import requests

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

CURRENT_GAMES_LIST="https://raw.githubusercontent.com/RavingSmurfGB/Game_Choice/main/games_list.txt"
RANDOM_PHRASE= [
    "Loki, the god of mischief has chosen: ",
    "I span the wheel and it came back with: ",
    "I've not rigged this but your game is: ",
    "Did you know you don't get taxed on your: ",
    "It was between WatchTogether and this, I thought you'd prefer this: "
]

def get_steam_game_link(game: str):
    """Polls the steam api for the game id returns game link
    """
    steam = requests.get(url="http://api.steampowered.com/ISteamApps/GetAppList/v0002/", timeout=60)
    if steam.ok:
        steam_games = steam.json()

        for game_dic in steam_games["applist"]["apps"]:
            if game == game_dic['name']:
                return f'https://store.steampowered.com/app/{game_dic["appid"]}'

    return None

def get_games_list():
    """function to pull down current games list from main branch
    """
    games_request = requests.get(url=CURRENT_GAMES_LIST, timeout=60)
    if games_request.ok:
        return [game.decode("utf-8").title().strip() for game in games_request.iter_lines()]

    return None

@bot.command(name="spin")
async def random_game(ctx):
    """Randomly chooses a game from the list
    """
    game = random.choice(list(get_games_list()))
    phrase = random.choice(RANDOM_PHRASE)
    steam_link = get_steam_game_link(game)

    if steam_link is not None:
        message = phrase + f"{game} \nURL can be found here: {steam_link}"
    else:
        message = phrase + f"{game}"

    await ctx.send(message)

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))
