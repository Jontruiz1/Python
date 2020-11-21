'''
Was planning on adding more fun commands to mess with but I stopped after a coinflip.
Give some suggestions for what to add
'''
import asyncio
import discord
import random
from datetime import datetime
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
            
    #A personal poll bot to see if anyone else wants to play a game, if it reaches the time that is passed in, it pings all the players that reacted to the message
    @commands.command()
    async def amongPoll(self, ctx, arg):
        roleId = 750560026208501800
        msg = await ctx.send(f"<@&{roleId}> React with :white_check_mark: to say yes to playing Among us at {arg}pm")
        await msg.add_reaction('✅')

        now = datetime.now()
        hour = int(now.strftime('%I'))
        minute = int(now.strftime('%M'))/60
        time = hour + minute
        argTime = float(arg)

        sleepTime = (argTime - time) * 3600

        await asyncio.sleep(int(sleepTime))

        message = await ctx.fetch_message(msg.id)

        users = []
        for reaction in message.reactions:
            async for user in reaction.users():
                users.append(user.id)

        del users[0]

        if(len(users) >= 8):
            for user in users:
                myid = f'<@{user}>'
                await ctx.send(f'{myid} Among Us?')
        else:
            await ctx.send('Less than 8 people reacted, no invites sent out')
            
def setup(bot):
    bot.add_cog(Fun(bot))
