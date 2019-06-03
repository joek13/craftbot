from discord.ext import commands
import discord
import websockets
import asyncio
from mcstatus import MinecraftServer

def _format_status(status):
    return f"{status.players.online}/{status.players.max} online | {status.description} | {status.latency}ms"

class Status(commands.Cog):
    """Commands to check the status of a Minecraft server."""

    def __init__(self, bot, cfg):
        self.bot = bot
        self.cfg = cfg
        
        self.server = MinecraftServer.lookup(self.cfg["server_ip"])

    @commands.Cog.listener()
    async def on_ready(self):
        # start running a periodic status checker
        loop = asyncio.get_event_loop()

        try:
            loop.create_task(self.periodically_update_presence())
        except asyncio.CancelledError:
            pass

    async def periodically_update_presence(self, interval=5):
        while True:
            try:
                await self.update_presence()
            except ws.exceptions.ConnectionClosed:
                pass
            await asyncio.sleep(interval)

    async def update_presence(self):
        """Updates the presence of the bot to reflect the server's status."""
        status_string = ""
        try:
            status = self.server.status()
            status_string = _format_status(status)
        except ConnectionRefusedError:
            status_string = "Offline"

        game = discord.Game(status_string) 
        await self.bot.change_presence(activity=game)

    @commands.command()
    async def status(self, ctx):
        """Gets the status of the server."""
        try:
            status = self.server.status()
            await ctx.send(_format_status(status))
        except ConnectionRefusedError:
            await ctx.send("The server is currently offline.")

