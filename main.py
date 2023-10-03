import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$reroll"):
        rolls = ["top", "jungle", "mid", "bot", "support"]
        people = message.content.removeprefix("$reroll").split()
        random_people = [f"rando{index}" for index in range(1, 6)]
        people.extend(random_people)
        people = people[0:5]
        random.shuffle(people)
        lines = [f"{roll}: {person}" for roll, person in zip(rolls, people)]
        out = "\n".join(lines)
        await message.channel.send(out)


discord_bot_api_key = os.getenv("DISCORD_BOT_API_KEY", "")
client.run(discord_bot_api_key)
