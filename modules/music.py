import discord
from discord import FFmpegPCMAudio, TextChannel
from discord.ext import commands
from discord.utils import get
from youtube_dl import YoutubeDL

class MusicCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}        

    def link_validation(self,url):
        if url.startswith("https://www.youtube.com/"):
            return True
        return False

    @commands.command()
    async def play(self, ctx, url):
        if self.link_validation(url):
            # bot join user channel
            channel = ctx.author.voice.channel
            if not channel:
                await ctx.send('You re not connected to any voice channel')
            else:
                voice = get(self.bot.voice_clients, guild = ctx.guild)
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()
                # bot is playing?
                if voice.is_playing():
                    voice.stop()
                # play current music
                with YoutubeDL(self.YDL_OPTIONS) as ydl:
                        info = ydl.extract_info(url, download = False)
                try:
                    voice.play(discord.FFmpegPCMAudio(info['url'], **self.FFMPEG_OPTIONS))
                    voice.volume = 100
                    voice.is_playing()
                except Exception as err:
                        print(err)
        else:
            await ctx.send('Invalid link')
        return

    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()

    @commands.command()
    async def stop(self,ctx):
        if voice.is_playing():
            await ctx.voice_client.stop()
            await ctx.send('Stop music...')
        await ctx.voice_client.disconnect()

async def setup(bot):
    await bot.add_cog(MusicCog(bot))