import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix='!', intents=intents)


phrases = [
    "Ты пидор",
    "Ты лох",
    "Ты моя няша"
]

@bot.event
async def on_ready():
    print(f'Бот {bot.user} успешно запущен!')
    print(f'ID бота: {bot.user.id}')

@bot.command(name='phrase', aliases=['фраза', 'random'])
async def random_phrase(ctx):
    """Выдает случайную фразу, удаляет команду и отмечает автора"""
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass 

    selected_phrase = random.choice(phrases)

    await ctx.send(f"{ctx.author.mention}, {selected_phrase}")

if __name__ == '__main__':
    bot.run(os.environ.get('DISCORD_TOKEN'))
