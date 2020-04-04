import discord
import os
import asyncio
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

access_token = os.environ["BOT_TOKEN"]
client.run('acess_token')
