import discord
TOKEN = 'OTg5MTg1NzU1Njg1NDU4MDIw.G7xUAU.EoxWxVvw7mYT6GA43fdzEee7EnQxAYLi4CQykk'
client = discord.Client()
@client.event
async  def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!Server'):
        await message.channel.send(f'{message.author.mention} crazywolves.aternos.me')  
client.run(TOKEN, bot=True)