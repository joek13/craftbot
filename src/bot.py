import discord
import config
from discord.ext import commands
from cogs import status

cfg = config.load_config()
bot = commands.Bot(command_prefix="++")

COGS = [status.Status]
def add_cogs(bot):
    for cog in COGS:
        bot.add_cog(cog(bot, cfg))

def run():
    add_cogs(bot)

    if cfg["token"] == "":
            raise ValueError(
                "No token has been provided. Please ensure that config.toml contains the bot token."
            )
            sys.exit(1)
    bot.run(cfg["token"])
