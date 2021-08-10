import discord
from discord.ext import commands
import validators
import datetime

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = 'e.', case_insensitive = True, intents= intents) #Ver prefixo

@bot.event
async def on_ready():
  print('Estou ligado')

lista = []

@bot.event
async def on_user_update(before, after):
  channel = bot.get_channel(739216493706739717)
  if before.id == 805145592606228491 and before.avatar != after.avatar: 
    counter = 0
    while True:
      counter += 1
      lista.append(counter)
      usuario = bot.get_user(805145592606228491)
      embedVar = discord.Embed(title="O Eki mudou de pfp dnv", description=f"[Antiga pfp]({before.avatar_url})", color=0x00ff00)

      embedVar.set_footer(text=f'Horário: {datetime.datetime.now().strftime("%H:%M:%S")}')
      embedVar.set_thumbnail(url = usuario.avatar_url)
      embedVar.add_field(name = 'Quantas vezes já aconteceu?', value=f'Já é a {sum(lista)}° vez no dia que isso acontece', inline=True)
    
      await channel.send(embed=embedVar)
      break
    
@bot.event
async def on_member_update(before, after):
    channel = bot.get_channel(739216493706739717) 
    if before.id == 805145592606228491 and before.name != after.name:
        await channel.send(f'nick mudado')

bot.run('TOKEN')
