# THIS IS YOUR MAIN BOT FILE

import discord
from discord.ext import commands

token = 'TOKEN'
prefix = "PREFIX"

admin_ids = {
    265737887805472768
} # Add the ids here of anyone who needs access to the extension commands

client = commands.Bot(command_prefix=prefix)
client.remove_command("help")

preload_extensions = ['example1', 'example2'] # These are the extensions that load when the bot starts.
loaded_extensions = [] # Don't touch, this is to keep track of extensions loaded.


@client.event
async def on_ready():
    print("Bot ready!")


# Contains everything related to extensions
@client.command()
async def extension(ctx, action, toy_extension):
    print(ctx.message.content + " - " + ctx.author.name + "#" + ctx.author.discriminator + " - " + ctx.guild.name)
    if ctx.author.id in admin_ids:
        # Loading Extension
        if action == "load":
            try:
                client.load_extension(toy_extension)
                print("Loaded extension {}.".format(toy_extension))
                loaded_extensions.append(toy_extension)
                await ctx.send("Loaded extension {} successfully!".format(toy_extension))
            except Exception as errorload:
                print("Failed to load extension {}. [{}]".format(toy_extension, errorload))
                await ctx.send("Failed to load extension {}.".format(toy_extension))
        # Unload Extension
        elif action == "unload":
            try:
                client.unload_extension(toy_extension)
                await ctx.send("Unloaded extension {} successfully!".format(toy_extension))
                loaded_extensions.remove(toy_extension)
                print("Unloaded extension {}.".format(toy_extension))
            except Exception as errorunload:
                print("Failed to unload extension {}. [{}]".format(toy_extension, errorunload))
                await ctx.send("Failed to unload extension {}.".format(toy_extension))
        # Reload ALL Loaded Extensions
        elif action == "reload" and toy_extension == "*":
            try:
                for reextension in loaded_extensions:
                    client.unload_extension(reextension)
                    loaded_extensions.remove(reextension)
                    client.load_extension(reextension)
                    loaded_extensions.append(reextension)
                    print("Reloaded extension {}!".format(reextension))

                print("Successfully reloaded all extensions!")
                await ctx.send("Successfully reloaded all extensions!")
            except Exception as err2:
                print("Failed to reload all extensions! [{}]".format(err2))
                await ctx.send("Failed to reload all extensions!")
        # Reload Extension
        elif action == "reload":
            try:
                client.unload_extension(toy_extension)
                loaded_extensions.remove(toy_extension)
                client.load_extension(toy_extension)
                loaded_extensions.append(toy_extension)
                print("Reloaded extension {} successfully!".format(toy_extension))
                await ctx.send("Reloaded extension {}!".format(toy_extension))
            except Exception as errorreload:
                print("Failed to reload extension {}. [{}]".format(toy_extension, errorreload))
                await ctx.send("Failed to reload extension {}.".format(toy_extension))
        else:
            await ctx.send("Unknown action!")

# Load extensions that load on startup and run the bot.
if __name__ == "__main__":
    for load_extension in preload_extensions:
        try:
            print("Loading {}...".format(load_extension))
            client.load_extension(load_extension)
            loaded_extensions.append(load_extension)
            print("Loaded {}!".format(load_extension))
        except Exception as error:
            print("{} cannot be loaded. [{}]".format(load_extension, error))
    client.run(token)
