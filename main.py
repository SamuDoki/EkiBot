import discord
from discord.ext import commands
import validators
import datetime

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = 'e.', case_insensitive = True, intents= intents)

@bot.event
async def on_ready():
  print('Estou ligado')

counter = 0

@bot.event
async def on_user_update(before, after):

  channel = bot.get_channel(739216493706739717) 
  if before.id == 805145592606228491 and before.avatar != after.avatar: 
    while True:
      counter += 1
      usuario = bot.get_user(805145592606228491)
      embedVar = discord.Embed(title="O Eki mudou de pfp dnv", description="Antiga pfp", color=0x00ff00)

      embedVar.set_footer(text=f'Já é a {counter}° vez no dia que isso acontece')
      embedVar.set_thumbnail(url = usuario.avatar_url)
      embedVar.add_field(name = 'o', value='Antiga pfp', inline=True)
    
      await channel.send(embed=embedVar)
      break

@bot.event
async def on_member_update(before, after):
    channel = bot.get_channel(739216493706739717) 
    if before.id == 805145592606228491 and before.name != after.name:
        await channel.send(f'nick mudado')

bot.run('ODY5NzIyMDkxMjcwODUyNjQ4.YQCV0Q.UtEEHEz0fNzMJC3ki-HTg5Wvw2Q')
