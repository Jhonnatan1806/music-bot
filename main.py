import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix = '!', intents = intents)

cogs = ['modules.members','modules.music']

async def main():
    # start the client
    async with bot:
        for cog in cogs:
            await bot.load_extension(cog)
        await bot.start(os.getenv('TOKEN'))

asyncio.run(main())