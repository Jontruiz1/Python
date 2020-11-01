import discord
import nacl
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

songs = asyncio.Queue()
play_next_song = asyncio.Event()


class AudioBot(commands.Cog):
    playing = ''
    queue = []

    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
        
    @bot.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @bot.command(pass_context=True)
    async def play(self, ctx, url):
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
        except:
            await ctx.send('Please join a channel first')

def setup(bot):
    bot.add_cog(AudioBot(bot))