import os
from threading import Thread
from flask import Flask

app = Flask(__name__)

def run():
    app.run(host='0.0.0.0', port=8092)  # Corrected port number

def keep_alive():
    t = Thread(target=run)
    t.start()

def start_bot():
    os.system('python3 main.py &')
    # Keep the Flask app alive in a separate thread
    keep_alive()

def stop_bot():
    os.system('pkill -f main.py')

if __name__ == "__main__":
    start_bot()
