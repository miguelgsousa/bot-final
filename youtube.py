import os
import urllib
import discord
import asyncio
from discord.ext import commands
from .utils.dataIO import dataIO
from .utils import checks
import requests
import aiohttp
from apiclient.discovery import build
import os

client = discord.Client()

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:
    import secreto

    token = secreto.token

class Skyton:
    def __init__(self, bot):
        self.bot = bot
        self.servers = dataIO.load_json("data/skyton/servers.json")
        self.uploads = dataIO.load_json("data/skyton/uploads.json")
        self.DEVELOPER_KEY = "AIzaSyBsiAshnAsyv5WX2H_5t9Y8DFWqdoPLH3k"
        self.YOUTUBE_API_SERVICE_NAME = "youtube"
        self.YOUTUBE_API_VERSION = "v3"

    def is_me(self, m):
        return m.author == self.bot.user

    async def playlist_checker(self):
        CHECK_DELAY = 60

        while self == self.bot.get_cog("Skyton"):
            youtube = build(self.YOUTUBE_API_SERVICE_NAME,self.YOUTUBE_API_VERSION,developerKey=self.DEVELOPER_KEY)

            ytchannel = youtube.channels().list(part='snippet,contentDetails', id="UCPZArGwSg9tykifitt-Ic1A").execute()
            uploadPL = ytchannel['items'][0]['contentDetails']['relatedPlaylists']['uploads']
            results = youtube.playlistItems().list(part='snippet,contentDetails',playlistId=uploadPL).execute()
            url = "https://youtube.com/watch?v="
            if results['pageInfo']['totalResults'] != self.uploads["UPLOADS"]:
                print("new vid.")
                self.uploads["UPLOADS"] = results['pageInfo']['totalResults']
                for vid in results['items']:
                    if vid['snippet']['position'] == 0:
                        vid_title = vid['snippet']['title']
                        vid_description = vid['snippet']['description']
                        vid_id = url + vid['snippet']['resourceId']['videoId']
                        break
                self.uploads["VID_TITLE"] = vid_title
                self.uploads["DESC"] = vid_description
                self.uploads["URL"] = vid_id
                for server in self.servers:
                    for chan in self.servers[server]:
                        print(chan)
                        channel_obj = self.bot.get_channel(chan)
                        if channel_obj is not None:
                            canal = discord.Object(id=414449863812710400)
                            em = discord.Embed(description='https://www.youtube.com/watch?v={}'.format(vid_id), colour=0xdb2724)
                            em.set_author(name='Skyton posted a new video!', icon_url='https://images-ext-1.discordapp.net/external/UQo7ZCgbGSC9oxLbnPjcCyz5zxD9ByI-MvMtytihJOQ/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/368787446894166037/b16c4b7cdfc015f3ea468e20cf070a8a.webp')
                            em.add_field(name='Video Title', value=vid_title)
                            em.add_field(name='Duration', value='videoDuration'),
                            em.set_thumbnail(url='https://yt3.ggpht.com/-PFnoIFfzibg/AAAAAAAAAAI/AAAAAAAABlw/2XRZhWeVTDI/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg')
                            em.set_image(url='https://i1.ytimg.com/vi/{}/hqdefault.jpg'.format(vid_id))
                            em.set_footer(text='If you do not want to receive notification of the new videos, click on the channel bell.',icon_url='https://cdn.discordapp.com/attachments/414502767881617408/435123830848225280/unnamed.png')
                            botmsg = await self.bot.client.send_message(canal, '@everyone', embed=em)
                            await self.bot.client.add_reaction(botmsg, ":youtube:436314272142721034")
                            dataIO.save_json("data/skyton/uploads.json", self.uploads)
                            await asyncio.sleep(CHECK_DELAY)

def check_folders():
    if not os.path.exists("data/skyton"):
        print("Creating data/skyton folder")
        os.makedirs("data/skyton")

def check_files():
    f = "data/skyton/servers.json"
    if not dataIO.is_valid_json(f):
        print("SKYTON: Creating empty servers.json...")
        dataIO.save_json(f, {})
    f = "data/skyton/uploads.json"
    if not dataIO.is_valid_json(f):
        print("SKYTON: Creating empty uploads.json...")
        dataIO.save_json(f, {"UPLOADS" : 0, "VID_TITLE" : "", "DESC" : "", "URL" :""})

def setup(bot):
    check_folders()
    check_files()
    n = Skyton(bot)
    loop = asyncio.get_event_loop()
    loop.create_task(n.playlist_checker())
    bot.add_cog(n)

client.run(token)

