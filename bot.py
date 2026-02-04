import discord

from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

WELCOME_CHANNEL_ID = 1364711496247939216

@bot.event
async def on_ready():
    print(f'Bot online come {bot.user}')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel is None:
        return

    embed = discord.Embed(
        title="Override",
        description=f"{member.mention} **Welcome to Override!**",
        color=discord.Color.orange(),
        timestamp=datetime.utcnow()
    )

    embed.set_footer(
        text="Copyright Override 2025® All rights reserved"
    )

    if member.guild.icon:
        embed.set_thumbnail(url=member.guild.icon.url)

    await channel.send(embed=embed)

bot.run("MTQ2ODcyNTM5NTM3MjI0OTE0MQ.GcrOj7.jBhVploS58KVlEDH2_ze4possvfn7pOPNB23lw")
