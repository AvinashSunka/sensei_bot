import os

import discord
from discord.ext import commands as discord_commands
from src.bot import myBot

def main() -> None:
    print("Starting the bot...")
    intents = discord.Intents.default()
    intents.message_content = True
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_TOKEN environment variable is not set")

    
    bot = myBot(command_prefix=discord_commands.when_mentioned_or("!"), intents=intents)
    bot.run(token)


if __name__ == "__main__":
    main()
