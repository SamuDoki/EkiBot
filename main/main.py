import discord
from discord.ext import commands
import validators
import datetime
import asyncio
import pytz

client = discord.Client()
tz = pytz.timezone('America/Sao_Paulo')

intents = discord.Intents.default()  # Para o negocio de pfp funcionar
intents.members = True  # Para o negocio de pfp funcionar

# Ver prefixo e caso escrevam o comando em maiusculo, o bot le msm assim
bot = commands.Bot(command_prefix='e.', case_insensitive=True, intents=intents)


@bot.event
async def on_ready():
    print('Estou ligado.')  # Vai mandar msg no terminal quando ligado


async def clearCounter24h():  # Função em Loop pra ver se chegou meia noite.
    while True:
        if datetime.datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%H:%M:%S") == '00:00:00':
            f = open("main/counter.txt")
            f.write("0")
            f.close
            print('Counter resetado com sucesso!')
        await asyncio.sleep(1)  # O programa roda a cada 1 segundo.

client.loop.create_task(clearCounter24h())  # Loop.


@bot.command()
async def count(ctx):  # Comando pra ver quantas vezes ele trocou de pfp.
    f = open("main/counter.txt", "r")
    await ctx.send(f'Total de vezes que o Ekin trocou de PFP hoje: {f.read()} vezes.')
    f.close()


@bot.event
async def on_user_update(before, after):
    channel = bot.get_channel(<ID DO CANAL>)  # Pegar id do canal

    # Pegar o id do usuário (no caso é o id da minha alt ai, vou esperar o eki voltar para atualizar)
    if before.id == <ID DO USUÁRIO> and before.avatar != after.avatar:
        f = open("main/counter.txt")  # Abre o arquivo "main/counter.txt".
        counterLeitura = f.read()  # Lê o arquivo.
        counterAtual = int(counterLeitura)  # Passa para a variável.
        f.close()  # Fecha o arquivo

        while True:

            counterSoma = counterAtual + 1
            # Passa o arquivo para string para escrever o arquivo.
            counter = str(counterSoma)
            f = open("main/counter.txt", "w")  # Abre o arquivo para escrever.
            f.write(counter)
            f.close()
            print('Counter atualizado com sucesso!')

            # Pegar o id do usuario e a tag dele (tipo Samudoki#1024 / ID)
            usuario = bot.get_user(<ID DO USUÁRIO>)
            # Titulo da embed, hyperlink da antiga pfp e a descrição
            embedVar = discord.Embed(title="O <NOME DO USUÁRIO> mudou de pfp dnv",
                                     description=f"[Antiga pfp]({before.avatar_url})", color=0x00ff00)

            # Rodapé da embed com a hora que mudou
            embedVar.set_footer(
                text=f'Horário: {datetime.datetime.now().strftime("%H:%M:%S")}')
            embedVar.set_thumbnail(url=usuario.avatar_url)  # Foto da pfp atual
            embedVar.add_field(name='Quantas vezes já aconteceu?',
                               value=f'Já é a {counter}° vez no dia que isso acontece', inline=True)  # Contador

            await channel.send(embed=embedVar)  # Mndaar embed

            break

bot.run('TOKEN')
