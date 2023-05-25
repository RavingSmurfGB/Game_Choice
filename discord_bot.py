import os
import random
import discord

CURRENT_GAMES_LIST="https://raw.githubusercontent.com/RavingSmurfGB/Game_Choice/main/games_list.txt"

class Client(discord.Client):
    '''A discord client that listens to specific messages in chat and 
    returns a message of a random game from the list
    '''
    async def on_ready(self):
        '''what to run when client is booted
        '''
        print('Logged on as', self.user)

    async def on_message(self, message):
        ''' This function gets triggered upon a message
        '''
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')


if "name" == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True
    client = Client(intents=intents)
    client.run('token')