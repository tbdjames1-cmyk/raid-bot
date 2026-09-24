import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# DM all members
@bot.command()

async def dmall(ctx, *, message):
    sent = 0
    failed = 0

    for member in ctx.guild.members:
        if not member.bot:
            try:
                await member.send(message)
                sent += 1
                print(f'Sent message to {member.name}')
                await asyncio.sleep(2)  # 2-second delay
            except Exception as e:
                failed += 1
                print(f'Could not send message to {member.name}: {e}')

    await ctx.send(
        f'Finished sending DMs.\n✅ Sent: {sent}\n❌ Failed: {failed}'
    )

# Send message to all text channels
@bot.command()

async def channels(ctx, *, message):
    sent = 0

    for channel in ctx.guild.text_channels:
        try:
            await channel.send(message)
            sent += 1
            await asyncio.sleep(1)  # Optional delay
        except discord.Forbidden:
            pass
        except Exception as e:
            print(f'Could not send to {channel.name}: {e}')

    await ctx.send(f'✅ Message sent to {sent} channels.')

bot.run('YOUR_BOT_TOKEN')
