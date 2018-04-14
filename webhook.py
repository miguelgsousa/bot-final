from async_webhook import WebhookClient, Embed
from datetime import datetime

client = WebhookClient()

em = Embed(
    color=0xdb2724, 
    description= video._url,
    timestamp=str(datetime.utcnow())
    ) 

em.set_author(name= 'Skyton posted a new video!', icon_url= user.name == 'Skyton' user.avatar_url )
em.add_field(name='Video Title',value= videoTitle)
em.add_field(name= 'Duration',value= videoDuration)
em.set_thumbnail('https://yt3.ggpht.com/-PFnoIFfzibg/AAAAAAAAAAI/AAAAAAAABlw/2XRZhWeVTDI/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg')
em.set_image(video.thubnail_url)
em.set_footer(text='If you do not want to receive notification of the new videos, click on the channel bell.',icon_url='https://blog.beekeeper.io/wp-content/uploads/2014/05/Youtube-button.png')
 await Client.send_message(Client.get_channel(default_notification_ann_channel), '@everyone', embed = em)

@client.on('start')
async def main():
    await client.send(embeds=em)

@client.on('error') # error handler, useful for larger apps
async def handler(error):
    pass

client.run('https://discordapp.com/api/webhooks/419910441020686336/5RhItDUQK7LydXPrR3RSn6wGzZI_4M8xxmmgL4ClE8RpLm7v7vBtYlU7hLxJybBu-_Ur')
