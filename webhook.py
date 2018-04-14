from async_webhook import WebhookClient, Embed
from datetime import datetime

client = WebhookClient()

em = Embed(
    color=0x00FFFF, 
    description='This is the **description** of the embed!',
    timestamp=str(datetime.utcnow())
    ) 

em.set_author(name='Author Goes Here', icon_url='https://i.imgur.com/rdm3W9t.png')
em.add_field(name='Test Field',value='Value of the field')
em.add_field(name='Another Field',value='1234')
em.set_thumbnail('https://i.imgur.com/rdm3W9t.png')
em.set_image('https://i.imgur.com/f1LOr4q.png')
em.set_footer(text='Here is my footer text',icon_url='https://i.imgur.com/rdm3W9t.png')

@client.on('start')
async def main():
    await client.send(embeds=em)

@client.on('error') # error handler, useful for larger apps
async def handler(error):
    pass

client.run('https://discordapp.com/api/webhooks/419910441020686336/5RhItDUQK7LydXPrR3RSn6wGzZI_4M8xxmmgL4ClE8RpLm7v7vBtYlU7hLxJybBu-_Ur')
