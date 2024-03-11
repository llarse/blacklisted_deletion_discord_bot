import discord
import os


BOT_TOKEN = os.getenv("BOT_TOKEN")
BLACKLISTED_USERS = os.getenv("BLACKLISTED_USERS")

intents = discord.Intents.default()
intents.messages = True  # Enable message intents for the bot

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'Logged in as {client.user} (ID: {client.user.id})')

@client.event
async def on_message(message):
  # Ignore messages from the bot itself
  if message.author == client.user:
    return

  # Check if the author's ID is in the blacklist
  if message.author.id in BLACKLISTED_USERS:
    print(f"Deleting message from blacklisted user: {message.author} ({message.author.id}) - {message.content}")
    await message.delete()

client.run(BOT_TOKEN)
