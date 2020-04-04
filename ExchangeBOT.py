import discord
import asyncio
import random
from discord import Member
from discord.ext import commands
from discord.ext.commands import Bot
from urllib.request import urlopen, Request
import urllib
import urllib.request
import bs4

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    id = message.author.id
    channel = message.channel

    if message.content.startswith("!exchange"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)

        url = "https://ko.valutafx.com/" + enc_location + "-KRW.htm"
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        exc_rate = bsObj.find("div", {"class":"rate-value"})
        rate = exc_rate.text

        await channel.send(rate)

    if message.content.startswith("!calculate"):
        learn = message.content.split(" ")
        location = learn[1]
        sum = eval(location)

        await channel.send(sum)


#@client.command(name="exchange", pass_context=True)
#async def exchange(txt):
#        learn = message.content.split(" ")
#        location = learn[1]
#        enc_location = urllib.parse.quote(location)

#        url = "https://ko.valutafx.com/" + enc_location + "-KRW.htm"
#        html = urllib.request.urlopen(url)

#        bsObj = bs4.BeautifulSoup(html, "html.parser")
#        exc_rate = bsObj.find("div", {"class":"rate-value"})
#        rate = exc_rate.text

#        await txt.send(rate)

#@client.command(name="multi", pass_context=True)
#async def multi(*args):
#        learn = message.content.split(" ")
#        location = learn[1]
#        enc_location = urllib.parse.quote(location)
#        sum = eval(enc_location)

#        await client.send(sum)

client.run('Njk1Mjc0NzUyNTM3MDAyMDM0.Xoc5iw.l_aAUL6rLQKQJcddCYiE68QpLs0')
