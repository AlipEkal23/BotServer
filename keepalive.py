import os
from threading import Thread
from flask import Flask

app = Flask(__name__)

bot_process = None
flask_port = 0  # Initialize with 0 for dynamic port assignment

@app.route('/')
def index():
    return "Alive"

def run():
    app.run(host='0.0.0.0', port=flask_port)

def keep_alive():
    global flask_port
    t = Thread(target=run)
    
    # Find an available port starting from 8091
    while True:
        try_port = flask_port + 1
        try:
            app.run(host='0.0.0.0', port=try_port, threaded=True)
            flask_port = try_port
            break
        except OSError:
            continue
    
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

# For testing purposes, you can uncomment the lines below:
# start_bot()
# print(f"Flask server is running on port {flask_port}")
