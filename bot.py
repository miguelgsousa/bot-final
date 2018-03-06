import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests
import io
import aiohttp
from datetime import datetime, timedelta

client = discord.Client()



@client.event
async def on_ready():
    await client.change_presence(
        game=discord.Game(type=0, name='with style'))

@client.event
async def on_member_join(member):
    await client.send_message(member,
                           'welcome to ' + member.server.name + ' ' + member.mention + '\n first read the rules in # welcome, if you want to call a person or a friend to serve you use this link: https://discord.gg/eRjQKEJ .       have a good time ;)')

    await client.add_roles(member)

@client.event
async def on_member_ban(user):
    channel = discord.utils.find(lambda c: c.name == 'geral', user.server.channels)
    embed = discord.Embed(title="I'm so sorry", description="the member **@{0.name}** was banned from the server".format(user), color=0xFF7F00

)
    embed.set_thumbnail(url=user.avatar_url)
    await client.send_message(channel, embed=embed)

@client.event
async def on_message(message):
    if message.content.lower().startswith('!ping') and not message.author.id == '419133912330272779':
        d = datetime.utcnow() - message.timestamp
        s = d.seconds * 1000 + d.microseconds // 1000
        await client.send_message(message.channel, ':ping_pong: Pong! {}ms'.format(s))


client.run('NDE5MTMzOTEyMzMwMjcyNzc5.DXzEMg.01PI1znwXf26ou-Om7nFAhxCAeg')
