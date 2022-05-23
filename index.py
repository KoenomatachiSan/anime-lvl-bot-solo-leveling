import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")

@bot.command()
async def teste(ctx):
    embed=discord.Embed(title="[KNM-MANGA] Solo Leveling", url="https://images-na.ssl-images-amazon.com/images/I/916fu0VFcnL.jpg", description="Wiki bot, com curiosidades e informações a respeito do anime em geral.")
    embed.set_thumbnail(url="https://images-na.ssl-images-amazon.com/images/I/916fu0VFcnL.jpg")
    embed.add_field(name="/knm solo-leveling personagens", value="Retornará uma lista com todos os personagens dos animes, podendo ser selecionados detalhes do mesmo.", inline=True)
    embed.add_field(name="/knm solo-leveling personagem ~id~", value="Retornará um resumo com todas as informações a respeito do personagem solicitado.", inline=True)
    embed.add_field(name="/knm solo-leveling help", value="Retornará uma lista de comandos e a descrição a respeito do bot.", inline=True)
    embed.set_footer(text="Desenvolvido por KNM TEAM")
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="http://www.twitch.tv/accountname"))
    print('My Ready is Body')


@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)

bot.run('OTc2Njk3NTQ0Nzk1MDk1MDUx.G4aAj1.a9nKfjm-gJoKsq5G9OXOeFkEGNRpLnKNkTiTuA')