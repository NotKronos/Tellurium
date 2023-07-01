import discord

from discord.ext import commands

import config

# Intents, some new discord shit that I hate

intents = discord.Intents.all()
intents.message_content = True
intents.typing = True
intents.presences = True


# Settings

bot_config: config = config.Config(config)

prefix: str = bot_config.prefix  # Command prefix used for legacy commands
use_status: bool = bot_config.use_status  # decides whether the bot will use custom presence status or not
status: str = bot_config.status  # said status
use_nickname: bool = bot_config.use_nickname  # bot will set its server display name to nickname
nickname: str = bot_config.nickname  # previous setting explains it
warnings: bool = bot_config.warnings  # setting it to false will supress "no administrator permission" warnings

client = commands.Bot(command_prefix=prefix, intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.command(name="prefix")
async def prefix(ctx):
    if ctx.message.author.guild_permissions.administrator:
        print("meow")


f = open("token", "r")
token = f.read()
f.close()

client.run(token)
