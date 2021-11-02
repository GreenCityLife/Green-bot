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

@client.event 
async def on_message(message): 
 if message.content.startswith(';help'):
  embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
  embedVar.add_field(name="Field1", value="hi", inline=False) 
  embedVar.add_field(name="Field2", value="hi2", inline=False) 
  await message.channel.send(embed=embedVar)

if __name__ == "__main__":
    bot.run(TOKEN)
