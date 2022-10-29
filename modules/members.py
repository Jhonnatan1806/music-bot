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

    @commands.command()
    async def server(self,ctx):
        embed = discord.Embed(title = f"{ctx.guild.name} Info", description = "Information of this Server", color = discord.Colour.blue())
        embed.add_field(name = '🆔Server ID', value = f"{ctx.guild.id}", inline = True)
        embed.add_field(name = '📆Created On', value = ctx.guild.created_at.strftime("%b %d %Y"), inline = True)
        embed.add_field(name = '👑Owner', value = f"{ctx.guild.owner}", inline = True)
        embed.add_field(name = '👥Members', value = f'{ctx.guild.member_count} Members', inline = True)
        embed.add_field(name = '💬Channels', value = f'{ctx.guild.text_channel_count} Text | {ctx.guild.voice_channel_count} Voice', inline = True)
        embed.add_field(name = '🌎Region', value = f'{ctx.guild.region}', inline = True)
        embed.set_thumbnail(url = ctx.guild.icon_url)
        embed.set_footer(text = "⭐ • Duo")    
        await ctx.send(embed = embed)

async def setup(bot):
    await bot.add_cog(MembersCog(bot))