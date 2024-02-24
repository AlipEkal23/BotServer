import discord
from discord.ext import commands
import random
import os
from threading import Thread
from flask import Flask

app = Flask(__name__)
bot_process = None

def run():
    app.run(host='0.0.0.0', port=8091)

def keep_alive():
    t = Thread(target=run)
    t.start()

def start_bot():
    global bot_process
    if bot_process is None:
        bot_process = os.system('python3 main.py &')
        keep_alive()

def stop_bot():
    global bot_process
    if bot_process is not None:
        os.system('pkill -f main.py')
        bot_process = None
        # Restart the bot after stopping it
        start_bot()

# Move start_bot() to the end, after bot setup
# Access the bot token from the environment variable
bot_token = os.environ.get('BOT_TOKEN')

# Create the bot instance
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def boton(ctx):
    start_bot()
    await ctx.send("Bot is now running!")

@bot.command()
async def botoff(ctx):
    stop_bot()
    await ctx.send("Bot is now stopped!")

if not bot_token:
    print("Bot token not found. Please set the 'BOT_TOKEN' environment variable.")
else:
    # Command: !pro
    @bot.command(name='ayam', description='seberapa ayam kah anda')
    async def pro_command(ctx):
        # Generate a random pro percentage between 0 and 100
        pro_percentage = random.randint(0, 100)
        # Send the pro percentage as a response
        await ctx.send(f"{ctx.author.mention}, kau {pro_percentage}% ayam!")

    # Command: !siapaayam
    @bot.command(name='siapaayam', description='Siapa yang paling ayam?')
    async def siapa_ayam_command(ctx):
        # List of user IDs to select from
        user_ids = [690982140522790912, 1169610305303756830, 1111204219609948190, 1045674581727391776, 823107148480249876, 1179308367534116916]
        # Get a random user based on their ID
        random_user_id = random.choice(user_ids)
        random_user = bot.get_user(random_user_id)
        if random_user:
            # Send the response mentioning the randomly selected user
            await ctx.send(f"Yang paling ayam ialah: {random_user.mention}!")
        else:
            await ctx.send("Tidak dapat menemukan pengguna untuk memilih.")

    # Command: !gei
    @bot.command(name='gei', description='seberapa gei kah anda')
    async def gei_command(ctx):
        # Generate a random percentage between 1 and 100
        random_percentage = random.randint(1, 100)
        # Send the response mentioning the user and displaying the random percentage
        await ctx.send(f"{ctx.author.mention}, anda {random_percentage}%! gei 🏳️‍🌈")

    # Event: Bot is ready
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')

    # Event: On message
    @bot.event
    async def on_message(message):
        # Ignore messages sent by the bot itself
        if message.author == bot.user:
            return
        # Check if the message mentions the bot
        if bot.user.mention in message.content:
            # Check if the author is the bot owner
            if message.author.id == 690982140522790912:  # Replace with your own user ID
                # Respond with a special message for the bot owner
                await message.channel.send(f"{message.author.mention} halo owner ganteng.")
            else:
                # Respond with a message for other users mentioning the bot
                await message.channel.send(f"{message.author.mention} halo ayam, orang yang ayam jangan tag gue.")
        # Check if the message contains "alip"
        if "alip" in message.content.lower():
            await message.channel.send("alip lagi tururururu , jangan tag or call")
        await bot.process_commands(message)

# Run the bot
bot.run(bot_token)
