from discord import Embed
from discord.ext import commands

class PingCommand():
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self, ctx):
        embed = Embed(title="Pong!", color=0xff0000)
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(PingCommand(bot))