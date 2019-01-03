# DiscordPyExtensionManager
Extension manager for discord.py, allowing load, unload, and reload of specific parts of your bot, as well as splitting your bot into multiple files.
# How to Use
Download the bot.py file and add your bot token into the token variable.
Place extensions in the same folder as the bot.py
Once you have placed an extension in, add the file name (eg. "example" for "example.py") to the list preload_extensions to load them on run.
Choose your prefix and change the prefix variable to your prefix.
Find your Discord ID and add it to the list owner_ids to enable the extension commands.
# Extension Commands Guide
We'll use the prefix "!" as it is the default prefix.
!extension load ext
- Loads the extension specified in ext.
!extension unload ext
- Unloads the extension specified in ext.
!extension reload ext
- Unloads and loads the extension specified in ext.
!extension reload *
- Unloads and loads all extensions.
