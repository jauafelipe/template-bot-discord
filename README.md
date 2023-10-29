<br clear="both">

<h1 align="center">I decided to launch this bot template for discord using Python</h1>

# REQUIREMENTS

# discord.py | python-dotenv

<h2 align="center">Start</h2>

# import

```py
import dotenv
dotenv.load_dotenv()
import os
import discord
from discord.ext import commands

# configure
```

# Right below

```py
TOKEN = os.environ.get("TOKEN") # token in .env
client = commands.Bot(command_prefix="your prefix", intents=discord.Intents.all())
```

# Intents can be configured manually too

```py
intents = discord.Intents.default()
intents.dm_messages = True
client = commands.Bot(command_prefix="your prefix", intents=intents)
```

# let's get it all up and put the bot to work, using an event decorator

```py
TOKEN = os.environ.get("TOKEN") # token in .env
client = commands.Bot(command_prefix="your prefix", intents=discord.Intents.all())

@client.event
async def ready_bot():
    print(f"{client.user}")


@client.event
async def send_mesage(message:discord.Message):
    if "Pong" in message.content.lower():
        await message.channel.send("Ping")


#use
client.run(TOKEN)
```

# simple? yes?, Now let's register your commands.cog

# create a commands folder, inside it put basicStart.py

```py
# I recommend using class
import discord
from discord.ext import commands


# you can inherit from commands.cog
# I strongly recommend reading the documentation to understand
class CommandsBasic(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    """YOUR COMMAND"""
    @commands.command(name="name of your command")
    async def command(self, ctx:commands.Context):
        await ctx.send("My primary command")
```

# ok, let's register your command.Cog, returning to main.py

```py
# import commands in main.py
from commands.basicStart import CommandsBasic
```

# now inside ready where the bot starts place add this

```py
@client.event
async def online():
    #add commands
    await client.add_cog(CommandsBasic(client))
    print(f"online in {client.user}")

```

# Now your bot is ready to be used
