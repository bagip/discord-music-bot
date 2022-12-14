import discord
from discord.ext import commands
from discord import member

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = """
        Komande na botu:
        !pomoc - Sve moguce komande pokazuje
        !pevaj ili !p <keywords> - Najde pesmu na youtube i peva Sale
        !queue ili !q - Pokazuje queue pesama
        !skip - Skipuje pesmu koja trenutno ide
        !clear - Brise sve iz queue
        !leave ili !l - Diskonekta bota
        !pause - Pauzira bota
        !resume - Ponovo pusta bota
        """

        self.text_channel_list = []

    #some debug info so that we know the bot has started    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        await self.send_to_all()  

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    @commands.command(name = "dog", help = "dog")
    async def dog(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/853680766956732416/1030245212955623476/strahinja.png")
    

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)