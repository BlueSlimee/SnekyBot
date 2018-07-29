from discord import Embed
from discord.ext import commands

class HelpCommand():
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def help(self, ctx):
        embed = Embed(title="Olá!", color=0xf0d0f0, description="Eu sou Sneky, um bot exemplar feito em Python para o [Vespertine Developers](https://discord.gg/rHwQEFs) (Um servidor de programação bem legal! Clique no nome para entrar)")
        embed.add_field(name="Onde acho o codigo do Sneky?", value="No Github!\nhttps://github.com/PerfectDreams/SnekyBot")
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.remove_command('help')
    bot.add_cog(HelpCommand(bot))