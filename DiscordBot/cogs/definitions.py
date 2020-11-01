'''
Credit to peterjayandrew
I didn't use the code but I might eventually so I'll leave it in here
Thank you for code
'''


import re
import discord
import requests
from discord.ext import commands
from bs4 import BeautifulSoup



def chunks_of(n, lst):
    '''splits a list into chunks of n'''
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

def chunks_of_words(n, string) -> list:
    '''Splits a string into chunks of words, with 'n' number of words per chunk
    
    Spaces are fused, so chunks_of_words(2, "foo bar baz boz") -> ["foo bar", "baz boz"]
    '''
    wordlst = re.split(r' +', string)
    return[' '.join(i) for i in chunks_of(n, wordlst)]
