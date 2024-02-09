import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! My name is {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'\U0001f44b')
    
@bot.command()
async def info(ctx):
    await ctx.send(f'Hi! Im Climate Savior, your friendly climate bot :)\n \n Im here to teach you all about climate change and how dangerous it is.\n I can also give a few ways YOU can help save the Earth!\n \n Do you know what climate change looks like? Type %earth for a start!')
    
@bot.command()
async def earth(ctx):
    img_name = random.choice(os.listdir('earthpics'))
    with open(f'earthpics/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def causes(ctx):
    await ctx.send(f'Curious about what causes those things? Here are the main causes of climate change:\n 1. Excessive use of fossil fuel for electricity\n 2. Deforestation -> no trees\n 3. Industrial wastes (harmful gases and substances)\n 4. Vehicle emmision\n 5. Refridgerators, air conditioners, aerosol sprays! They all emmit CFC gases.\n \n \u2639\uFE0F \u2639\uFE0F \n \n Now are you wondering how you can contribute in preventing all this from getting worse? Type %prevent!')

@bot.command()
async def prevent(ctx):
    await ctx.send(f'Here are a few actions you can implement in your daily life to help stop climate change!\n 1. Turn off / unplug electronic devices when not in use \n 2. Walk or ride a bike more often! Its also healthier for you! :) \n 3. Use public transport when you can \n 4. Consume less meat (they produce a lot of harmful gases in the making process!)\n 5. Reduce (think twice before you buy something!)\n 6. Reuse (ditch one time use items from now on!) \n 7. RECYCLEEEEE \n 8. Type %recycle to see some fun ideas you can transform your waste products into!\n \n \U0001f642 \U0001f642')

@bot.command()
async def recycle(ctx):
    img_name2 = random.choice(os.listdir('recyclingideas'))
    with open(f'recyclingideas/{img_name2}', 'rb') as f:
        picture2 = discord.File(f)
    await ctx.send(file=picture2)

bot.run("TOKEN")
