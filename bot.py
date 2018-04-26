import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import io
import re
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
    await client.change_presence(game=discord.Game(type=3, name='the events on the server'))

@client.event
async def on_member_join(member):
    await client.send_message(member,'-  Helo **' + member.name + '** welcome to **' + member.server.name + '** !  - \n First read the rules in # welcome, if you want to call a person or a friend to serve you use this link:https://discord.gg/eRjQKEJ \n have a good time :wink:')
    await client.add_roles(member)
    
@client.event
async def on_member_message(member, message):
    if len(message.member.content) > 20:
        Medion_user = discord.utils.get(member.server.roles, name="Medion user")
        await client.add_roles(member, Medion_user)    
    
@client.event
async def on_message(message):
    if message.content.lower().startswith('!ping') and not message.author.id == '419133912330272779':
        d = datetime.utcnow() - message.timestamp
        s = d.seconds * 1000 + d.microseconds // 1000
        await client.send_message(message.channel, ':ping_pong: Pong! {}ms'.format(s))

    if message.content.startswith('!advert'):
        role = discord.utils.get(message.server.roles, name='Admin')
        mensagem = message.content[8:]
        canal = discord.utils.find(lambda c: c.name == 'adverts', message.server.channels)
        em = discord.Embed(description=mensagem, colour=0xdb513a)
        em.set_author(name='Notice of moderation!', icon_url=message.author.avatar_url)
        em.set_footer(text='Att.{}, Skyton server admin.'.format(message.author.name))
        await client.send_message(canal, '@everyone', embed=em)
 
    if message.content.lower().startswith("!ban"):
        await client.delete_message(message)
        role = discord.utils.get(message.server.roles, name='Admin')
        role = discord.utils.get(message.server.roles, name='Ban')
        author = message.author
        member_ban = message.mentions[0]
        em = discord.Embed(title=" **THIS WAY YOU'RE GONNA KILL DADDY!** ",description="Moderator **{}** banned member **{}** from server".format(author.name, member_ban),color=0xFF7F00)
        em.set_thumbnail(url=member_ban.avatar_url)
        ban = await client.ban(member_ban)
        await client.send_message(ban, message.channel, embed=em)
    
    if len(message.content) > 325:
        await client.delete_message(message)

    if message.channel == client.get_channel('414445398212476928'):
        await client.add_reaction(message, "😐")
        
    if message.author.id == ('159985870458322944'):
        await client.add_reaction(message, "😐")
        
    if message.author.id == ('155149108183695360'):
        await client.add_reaction(message, "😐")
        
client.run(token)
