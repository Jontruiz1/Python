import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def add(self, ctx, *args):
        sum = 0
        for a in args:
            sum += float(a)
        await ctx.send(f'Result is {sum}')
    
    @commands.command()
    async def sub(self, ctx, *args):
        difference = float(args[0])
        for x in range(1, len(args)):
            difference -= float(args[x])
        await ctx.send(f'Result is {difference}')
    
    @commands.command() 
    async def mult(self, ctx, *args):
        prod = float(args[0])
        for x in range(1, len(args)):
            prod *= float(args[x])
        await ctx.send(f'Result is {prod}')
    
    @commands.command()
    async def div(self, ctx, *args):
        try:
            quot = float(args[0])
            for x in range(1, len(args)):
                quot /= float(args[x])
            await ctx.send(f'Result is {quot}')
        except ZeroDivisionError:
            await ctx.send('Error: division by zero')

    @commands.command()
    async def mod(self, ctx, *args):
        try:
            modulo = float(args[0])
            for x in range(1, len(args)):
                modulo %= float(args[x])
            await ctx.send(f'Result is {modulo}')
        except:
            await ctx.send('Error: modulus by zero')
            
    @commands.command()
    async def pow(self, ctx, arg1, arg2):
        num1 = float(arg1)
        num2 = float(arg2)

        await ctx.send(f'Result is {num1 ** num2}')
def setup(bot):
    bot.add_cog(Calculator(bot))
