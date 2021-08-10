import discord
from discord.ext import commands
import validators
import datetime

intents = discord.Intents.default() #Para o negocio de pfp funcionar
intents.members = True #Para o negocio de pfp funcionar

bot = commands.Bot(command_prefix = 'e.', case_insensitive = True, intents= intents) #Ver prefixo e caso escrevam o comando em maiusculo, o bot le msm assim

@bot.event
async def on_ready():
  print('Estou ligado') #Vai mandar msg no terminal quando ligado

lista_contador = [] #Lista que vai contar quantas vezes o eki mudou de pfp 

@bot.event
async def on_user_update(before, after):
  channel = bot.get_channel(739216493706739717) #Pegar id do canal
  if before.id == 805145592606228491 and before.avatar != after.avatar: #Pegar o id do usuário (no caso é o id da minha alt ai, vou esperar o eki voltar para atualizar) 
    counter = 0 #Contar as pfps
    while True:
      counter += 1
      lista.append(counter) 
      usuario = bot.get_user(805145592606228491) #Pegar o id do usuario e a tag dele (tipo Samudoki#1024 / ID)
      embedVar = discord.Embed(title="O Eki mudou de pfp dnv", description=f"[Antiga pfp]({before.avatar_url})", color=0x00ff00) #Titulo da embed, hyperlink da antiga pfp e a descrição

      embedVar.set_footer(text=f'Horário: {datetime.datetime.now().strftime("%H:%M:%S")}') #Rodapé da embed com a hora que mudou
      embedVar.set_thumbnail(url = usuario.avatar_url) #Foto da pfp atual
      embedVar.add_field(name = 'Quantas vezes já aconteceu?', value=f'Já é a {sum(lista)}° vez no dia que isso acontece', inline=True) #Contador
    
      await channel.send(embed=embedVar) #Mndaar embed
      break
    
"""@bot.event
async def on_member_update(before, after):
    channel = bot.get_channel(739216493706739717) 
    if before.id == 805145592606228491 and before.name != after.name:
        await channel.send(f'nick mudado')""" #Ainda testando esse comando, se funcionar eu adiciono

bot.run('TOKEN')
