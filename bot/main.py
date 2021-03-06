import os
from discord.ext import commands

bot = commands.Bot(command_prefix=";",description="Your description here")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    activity = discord.Game(name="Netflix") 
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

if __name__ == "__main__":
    bot.run(TOKEN)
