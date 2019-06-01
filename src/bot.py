import discord
import config
from discord.ext import commands

cfg = config.load_config()
bot = commands.Bot(command_prefix="++")

COGS = []
def add_cogs(bot):
    for cog in COGS:
        bot.add_cog(cog(bot))

def run():
    add_cogs(bot)

    bot.run(token=cfg["token"])
