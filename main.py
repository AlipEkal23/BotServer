import discord
from discord.ext import commands
import random
import os

bot_token = os.environ.get('BOT_TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def boton(ctx):
    await ctx.send("Bot is now running!")

@bot.command()
async def botoff(ctx):
    await ctx.send("Bot is now stopped!")

if not bot_token:
    print("Bot token not found. Please set the 'BOT_TOKEN' environment variable.")
else:
    @bot.command(name='ayam', description='seberapa ayam kah anda')
    async def pro_command(ctx):
        pro_percentage = random.randint(0, 100)
        await ctx.send(f"{ctx.author.mention}, kau {pro_percentage}% ayam!")

    @bot.command(name='siapaayam', description='Siapa yang paling ayam?')
    async def siapa_ayam_command(ctx):
        user_ids = [690982140522790912, 1169610305303756830, 1111204219609948190, 1045674581727391776, 823107148480249876, 1179308367534116916]
        random_user_id = random.choice(user_ids)
        random_user = bot.get_user(random_user_id)
        if random_user:
            await ctx.send(f"Yang paling ayam ialah: {random_user.mention}!")
        else:
            await ctx.send("Tidak dapat menemukan pengguna untuk memilih.")

    @bot.command(name='gei', description='seberapa gei kah anda')
    async def gei_command(ctx):
        random_percentage = random.randint(1, 100)
        await ctx.send(f"{ctx.author.mention}, anda {random_percentage}%! gei 🏳️‍🌈")

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        if bot.user.mention in message.content:
            if message.author.id == 690982140522790912:
                await message.channel.send(f"{message.author.mention} halo owner ganteng.")
            else:
                await message.channel.send(f"{message.author.mention} halo ayam, orang yang ayam jangan tag gue.")
        if "alip" in message.content.lower():
            await message.channel.send("alip lagi tururururu , jangan tag or call")
        await bot.process_commands(message)

    bot.run(bot_token)
