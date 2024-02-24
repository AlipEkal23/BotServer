import os
from threading import Thread
from flask import Flask

app = Flask(__name__)
bot_process = None

def run():
    app.run(host='0.0.0.0', port=3000)  # Change port number to 3000

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

@app.route('/')
def home():
    return 'YaY Your Bot Status Changed✨'

if __name__ == "__main__":
    start_bot()
