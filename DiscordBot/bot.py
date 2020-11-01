import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

bot.load_extension('cogs.Tester')
bot.load_extension('cogs.math.basicmath.Calculator')
bot.load_extension('cogs.Fun')
bot.load_extension('cogs.Scraper')
bot.load_extension('cogs.AudioBot')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def shutdown(ctx):
    await ctx.send('Goodnight owo')
    print('Logging off')
    await bot.close()

@bot.command()
async def restart(ctx):
    await ctx.send('Reloading extensions')
    bot.reload_extension('cogs.Tester')
    bot.reload_extension('cogs.math.basicmath.Calculator')
    bot.reload_extension('cogs.Fun')
    bot.reload_extension('cogs.Scraper')
    bot.reload_extension('cogs.AudioBot')
    print('Reloaded extensions')
    await ctx.send('All extensions reloaded')

bot.run('TOKEN')
