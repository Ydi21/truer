import discord
import os
from discord.ext import commands, tasks
from itertools import cycle


# prefix
client = commands.Bot(command_prefix='.') 

status = cycle(['T', 'Tr', 'Tru', 'True', 'True!'])

# starts status loop
@client.event 
async def on_ready():
    change_status.start() 
    print('Bot rdy')

# status loop
@tasks.loop(seconds=5) 
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

# ping command
@client.command() 
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

# true ping
@client.event 
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send('{}'.format(message.author.mention) + ", True!" )

# bot token
client.run(os.environ['DISCORD_TOKEN'])
