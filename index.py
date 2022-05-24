import discord
from discord.ext import commands
import requests

#########################################
# Import database config                #
#########################################
request_database = requests.get(url = "https://raw.githubusercontent.com/knmsn/anime-lvl-api/main/endpoints_db/solo_leveling.json", params = {})
database = request_database.json()

#########################################
# Get .env variables
#########################################
lang_selected = "pt-br"

#########################################
# Set config database variables         #
#########################################
forDB_thumbnail_image = database[lang_selected]['thumbnail_image']
forDB_bot_name = database[lang_selected]['name']
forDB_command_prefix = database[lang_selected]['prefix']
forDB_description=database[lang_selected]['description']
forDB_characters=database[lang_selected]['database']['characters']

# Set commands from DB
forDB_command_help=database[lang_selected]['commands']['help']

bot = commands.Bot(command_prefix=forDB_command_prefix, description=forDB_description)
bot.remove_command('help')

@bot.command()
async def ajuda(ctx):
    embed=discord.Embed(title=f"[KNM-MANGA] {forDB_bot_name}", url=forDB_thumbnail_image, description=forDB_command_help['header'])
    embed.set_thumbnail(url=forDB_thumbnail_image)
    for x in forDB_command_help['embeds']:
        embed.add_field(name=x['title'], value=x['description'], inline=False)
    embed.set_footer(text=forDB_command_help['footer'])
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed=discord.Embed(title=f"[KNM-MANGA] {forDB_bot_name}", url=forDB_thumbnail_image, description=forDB_command_help['header'])
    embed.set_thumbnail(url=forDB_thumbnail_image)
    for x in forDB_command_help['embeds']:
        embed.add_field(name=x['title'], value=x['description'], inline=False)
    embed.set_footer(text=forDB_command_help['footer'])
    await ctx.send(embed=embed)

@bot.command()
async def personagens(ctx):
    embed=discord.Embed(title=f"[KNM-MANGA] {forDB_bot_name}", url=forDB_thumbnail_image, description="Abaixo está a lista com todos os personagens.")
    embed.set_thumbnail(url=forDB_thumbnail_image)
    for x in forDB_characters:
        embed.add_field(name=f"{x['id']} - {x['name']}", value=x['type'], inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def characters(ctx):
    embed=discord.Embed(title=f"[KNM-MANGA] {forDB_bot_name}", url=forDB_thumbnail_image, description="Abaixo está a lista com todos os personagens.")
    embed.set_thumbnail(url=forDB_thumbnail_image)
    for x in forDB_characters:
        embed.add_field(name=f"{x['id']} - {x['name']}", value=x['type'], inline=False)
    await ctx.send(embed=embed)

# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')

# @bot.command()
# async def sum(ctx, numOne: int, numTwo: int):
#     await ctx.send(numOne + numTwo)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Coding ();"))
    print('My Ready is Body')


@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)

bot.run('OTc2Njk3NTQ0Nzk1MDk1MDUx.G4aAj1.a9nKfjm-gJoKsq5G9OXOeFkEGNRpLnKNkTiTuA')