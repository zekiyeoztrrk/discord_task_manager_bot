import discord
from discord.ext import commands
from database import create_table
from commands import add_task_command, delete_task_command, show_tasks_command, complete_task_command

# Veritabanı tablosu
create_table()

# İzinler
intents = discord.Intents.default()
intents.message_content = True  

# Botu başlat
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def add_task(ctx, *, description: str):
    await add_task_command(ctx, description)

@bot.command()
async def delete_task(ctx, task_id: int):
    await delete_task_command(ctx, task_id)

@bot.command()
async def show_tasks(ctx):
    await show_tasks_command(ctx)

@bot.command()
async def complete_task(ctx, task_id: int):
    await complete_task_command(ctx, task_id)

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'  # Bot tokeni
bot.run(TOKEN)
