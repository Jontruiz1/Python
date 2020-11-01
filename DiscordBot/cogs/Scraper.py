import discord
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

try:
    import definitions
except ModuleNotFoundError:
    from cogs import definitions

from discord.ext import commands
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix='>')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
options = FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Firefox(firefox_options=options)


class Scraper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def rlPatch(self, ctx):
        driver.get('https://www.rocketleague.com/news/?cat=7-5aa1f33-rqfqqm')
        driver.find_element_by_xpath('//img[@alt="article-image"]').click()

        URL = driver.current_url
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        updates = soup.find('div', class_="column small-12 medium-10 large-10 page-content article")

        if len(updates.get_text()) < 2000:
            await ctx.send(updates.get_text())
        else:
            filename = f"Rocket League {soup.find('h1').get_text()}.txt"

            with open(filename, "w") as file:
                file.write(f"Rocket League {updates.get_text()}")
        
            await ctx.send(file=discord.File(f"{filename}"))
    
    ''' Parsing Valorants updates html pages is annoying and i don't wanna deal with it rn
    @commands.command()
    async def valPatch(self, ctx):
        driver.get('https://playvalorant.com/en-us/news/')
        driver.find_element_by_xpath('//a[@href="/en-us/news/game-updates/valorant-patch-notes"]').click()

        URL = driver.current_url
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        updates = soup.find('')
    '''

    @commands.command()
    async def phasPatch(self, ctx):
        URL = 'https://game-updates.info/phasmophobia'
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        updates = soup.find('div', class_='tabcontent update')

        if len(updates.get_text()) < 2000:
            await ctx.send(updates.get_text())
        else:

            #await ctx.send(definitions.chunks_of_words(900, updates.get_text()))
            
            filename = f"Phasmophobia {updates.find('h1').get_text()}.txt"

            with open(filename, "w") as file:
                file.write(f"Phasmophobia {updates.get_text()}")
        
            await ctx.send(file=discord.File(f"{filename}"))
            
            
            
def setup(bot):
    bot.add_cog(Scraper(bot))