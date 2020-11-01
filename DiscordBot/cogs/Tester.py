'''
Alot of these commands are basically useless, I just wanted some commands to test out if the bot was running or if it actually responded to commands
You don't have to include these
'''

import discord
from datetime import datetime
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

class Tester(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')

    @commands.command()
    async def pong(self, ctx):
        await ctx.send('ping')

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('hello!')

    @commands.command()
    async def date(self, ctx):
        now = datetime.now()
        dt_string = now.strftime("%B %d, %Y %H:%M:%S")
        await ctx.send(dt_string)	


def setup(bot):
    bot.add_cog(Tester(bot))
