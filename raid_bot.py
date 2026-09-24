import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("=" * 50)
    print(f"Logged in as {bot.user}")
    print(f"Bot ID: {bot.user.id}")
    print("=" * 50)

@bot.command()
async def dmall(ctx, *, message):
    print(f"\nStarting DM All in {ctx.guild.name}")

    sent = 0
    failed = 0

    for member in ctx.guild.members:
        if not member.bot:
            try:
                await member.send(message)
                sent += 1
                print(f"[SUCCESS] Sent DM to {member}")

                await asyncio.sleep(2)

            except Exception as e:
                failed += 1
                print(f"[FAILED] {member} - {e}")

    print("\nDM ALL COMPLETE")
    print(f"Sent: {sent}")
    print(f"Failed: {failed}")

@bot.command()
async def channels(ctx, *, message):
    print(f"\nStarting channel broadcast in {ctx.guild.name}")

    sent = 0

    for channel in ctx.guild.text_channels:
        try:
            await channel.send(message)
            sent += 1
            print(f"[SUCCESS] Sent to #{channel.name}")

            await asyncio.sleep(1)

        except Exception as e:
            print(f"[FAILED] #{channel.name} - {e}")

    print("\nCHANNEL BROADCAST COMPLETE")
    print(f"Messages sent to {sent} channels")

bot.run(TOKEN)
