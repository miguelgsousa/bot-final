import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import io
import re
import aiohttp
from datetime import datetime, timedelta
import os
from twitch import TwitchClient

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
                           '-  Helo **'+ member.name +'** welcome to **'+ member.server.name +'** !  - \n First read the rules in # welcome, if you want to call a person or a friend to serve you use this link:https://discord.gg/eRjQKEJ \n have a good time :wink:')
    
    await client.add_roles(member)

@client.event
async def on_member_ban(user):
    channel = discord.utils.find(lambda c: c.name == 'general', user.server.channels)
    embed = discord.Embed(title=" **THIS WAY YOU'RE GONNA KILL DADDY!** ", description="the member **@{0.name}** was banned from the server".format(user), color=0xFF7F00

)
    embed.set_thumbnail(url=user.avatar_url)
    await client.send_message(channel, embed=embed)

@client.event
async def on_message(message):
    if message.content.lower().startswith('!ping') and not message.author.id == '419133912330272779':
        d = datetime.utcnow() - message.timestamp
        s = d.seconds * 1000 + d.microseconds // 1000
        await client.send_message(message.channel, ':ping_pong: Pong! {}ms'.format(s))
    
    if message.content.lower().startswith('!diz'):
       mensagem = re.sub('!diz ', '', message.content)
       canaltxt = mensagem.split(' ', 1)
       canaltxt = str(canaltxt[0])
       mensagem = re.sub(canaltxt, '', mensagem)
       canal = discord.utils.find(lambda c: c.name == canaltxt or c.id == canaltxt or c.mention == canaltxt, message.author.server.channels)
       await client.send_message(canal, mensagem)

    if len(message.content) > 325:
        await client.delete_message(message)
     

@client.event
async def on_member_update(memberBEF,memberAFT):
    if len(memberBEF.roles) != 1:
        for cargo in memberBEF.roles:
            if (cargo.name == "Master" and memberAFT.game.type == 1):
                client = TwitchClient(client_id = twitchClientID)
                channel = client.channels.get_by_id(twitchChannelID)
                streamTitle = channel.status
                gameTitle = channel.game

                print('%s Goularte started streaming. Announced with @everyone in channel %s.' % (time_now(), default_twitch_ann_channel))

                em = discter(text = "Se não quiser mais receber notificações sobre as streams do Goularte, clique no sino em cima dessa página para mutar esse canal, assim: http://bit.ly/mutarcanal")
                em.set_thumord.Embed(description = 'http://twitch.tv/g0ularte', colour=0x4B367C)
                em.set_foobnail(url = "https://static-cdn.jtvnw.net/jtv_user_pictures/6b4206db-8f52-4662-a64f-e2098a9b8244-profile_image-70x70.png")
                em.set_author(name="Goularte está live na Twitch!", url="http://twitch.tv/g0ularte", icon_url=memberAFT.avatar_url)
                em.add_field(name = "Jogando", value = gameTitle, inline = True)
                em.add_field(name = "Título da Stream", value = streamTitle, inline = True)
                await client.send_message(client.get_channel(default_twitch_ann_channel), '@everyone', embed = em)    
    
client.run(token)
