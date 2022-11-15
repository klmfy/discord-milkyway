from discord.ext import commands
import discord
TOKEN = 'MTA0MTk4NTM5Mjk3MjQxNTAyNg.GvsThi.EttVS_CSQBSFsQhiAALTiqhGELWlRQQH4dRFWo'
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
client = discord.Client()
@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!Server'):
        await message.channel.send(f'{message.author.mention} milkiway.aternos.me:58562')
@bot.event
async def on_ready():
    print("Bot started")
@bot.event
async def on_member_join(member):
    role = member.guild.get_role(role_id=989847812755820558)
    await member.add_roles(role)
bot.run(TOKEN)
client.run(TOKEN, bot=True)

