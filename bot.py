import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import io
import aiohttp
from datetime import datetime, timedelta
import os

client = discord.Client()

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:
    import secreto
    token = secreto.token

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
    channel = discord.utils.find(lambda c: c.name == 'general', user.server.channels)
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

@client.event
if message.content.lower().startswith('/diz'):
        mensagem = re.sub('/diz ', '', message.content)
        canaltxt = mensagem.split(' ', 1)
        canaltxt = str(canaltxt[0])
        mensagem = re.sub(canaltxt, '', mensagem)
        canal = discord.utils.find(lambda r: r.name == canaltxt or r.id == canaltxt or r.mention == canaltxt, message.author.server.channels)
        await client.send_message(canal, mensagem)

client.run(token)