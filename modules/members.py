from discord.ext import commands

import discord

class MembersCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # register events, instead of using @Bot.events()
    @commands.Cog.listener() 
    async def on_ready(self):
        print('Adriana UwU is now online')

    # Instead of bot.command()
    @commands.command()
    async def ping(self,ctx):
        await ctx.send('pong')

async def setup(bot):
    await bot.add_cog(MembersCog(bot))