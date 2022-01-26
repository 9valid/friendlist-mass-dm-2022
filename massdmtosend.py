import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send(' @everyone ** Hostile releasing soon: ** https://discord.com/oauth2/authorize?client_id=738311451802075177&scope=bot&permissions=8 | https://discord.gg/aXJcu3Zrny')
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run("mfa.3hgUS9WTa0Unq6-Um6mtkDgSCDVbJCUjFAzXc3xWA_eJkCe7Qk3ZuGsMlnR6WILK-_3lD8PlMS5lLq6g_r4o", bot=False)
