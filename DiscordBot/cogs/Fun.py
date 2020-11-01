'''
Was planning on adding more fun commands to mess with but I stopped after a coinflip.
Give some suggestions for what to add
'''

import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix = '>')

class Fun(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
    
    @commands.command()
    async def coinflip(self, ctx):
        coin = random.randint(0,1)
        if(coin == 1):
            await ctx.send("Heads!")
        else:
            await ctx.send("Tails!")

def setup(bot):
    bot.add_cog(Fun(bot))
