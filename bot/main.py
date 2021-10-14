import os
from discord.ext import commands

activity = discord.Game(name="Geometry Dash")
bot = commands.Bot(command_prefix=";", activity=activity, status=discord.Status.idle)
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

if __name__ == "__main__":
    bot.run(TOKEN)
