# This is extension example 1

from discord.ext import commands
import discord


class Example1:
    def __init__(self, client):
        self.client = client

    # Basic hello Command
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")
    
    #Basic on_message Event
    @commands.event
    async def on_message(self, message):
        print("Message occured!")


# Makes the extension loadable
def setup(client):
    client.add_cog(Example1(client))
