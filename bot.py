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

msgban = discord.Embed(title='For one or more reasons you have been banned from skyton server!',description='If you think it was an unfair ban between' '[ in this link ](' + "https://goo.gl/kDKqhF" + ')' 'revoke your ban',colour=0xFF7F00)                            

msgban3 = discord.Embed(title='You have been banned from skyton server!',description='You have been banned automatically banned for violating rule number 9 of the server,enter' '[ this link ](' + "https://goo.gl/kDKqhF" + ')' 'if any mistake has been made',colour=0xFF7F00)                            

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(type=3, name='the events on the server'))

@client.event
async def on_member_join(member):
    em = discord.Embed(title='-  Helo **' + member.name + '** welcome to **' + member.server.name + '** ! -',description='First read the rules in # welcome, if you want to call a person or a friend to serve you use this' '[ link ](' + "https://discord.gg/eRjQKEJ" + ')''\n have a good time :wink:',colour=0xFF7F00)
    await client.send_message(member, embed=em)
    await client.add_roles(member) 
    
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
        user = message.mentions[0]
        em = discord.Embed(title=" **THIS WAY YOU'RE GONNA KILL DADDY!** ",description="Moderator **{}** banned member **{}** from server".format(author.name, user),color=0xFF7F00)
        em.set_thumbnail(url=user.avatar_url)
        await client.send_message(user, embed=msgban)
        msgchannel = await client.send_message(message.channel, embed=em)
        await client.add_reaction(msgchannel, "😮")
        await client.ban(user)
    
    if len(message.content) > 325:
        await client.delete_message(message)

    if message.content.lower().startswith("https://www.xvideos.com"):
        await client.delete_message(message)
        user = message.author
        msgban2 = discord.Embed(title=" **THIS WAY YOU'RE GONNA KILL DADDY!** ",description="The member **{}** was automatically banned for violating rule number 9 of the server".format(user),color=0xFF7F00)
        msgchannel = await client.send_message(message.channel, embed=msgban2)
        await client.add_reaction(msgchannel, "😮")
        await client.send_message(user, embed=msgban)
        await client.ban(user)
        
    if message.content.lower().startswith("http://www.redtube.com"):
        await client.delete_message(message)
        user = message.author
        msgban2 = discord.Embed(title=" **THIS WAY YOU'RE GONNA KILL DADDY!** ",description="The member **{}** was automatically banned for violating rule number 9 of the server".format(user),color=0xFF7F00)
        msgchannel = await client.send_message(message.channel, embed=msgban2)
        await client.add_reaction(msgchannel, "😮")
        await client.send_message(user, embed=msgban)
        await client.ban(user)    
        
    if message.content.lower().startswith("https://discord.gg"):
        await client.delete_message(message)
        user = message.author
        await client.send_message(message.channel, "Please do not send invitation {}#{}" .format(user.name,user.discriminator))      
        
    if message.channel == client.get_channel('414445398212476928'):
        await client.add_reaction(message, "😐")
        
    if message.author.id == ('159985870458322944'):
        await client.add_reaction(message, "😐")
        
    if message.author.id == ('155149108183695360'):
        await client.add_reaction(message, "😐")
        
client.run(token)
