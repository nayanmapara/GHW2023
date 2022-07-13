from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Blahaj Bot"

def run():
  app.run(host='0.0.0.0', port=81)
  
def keeping_alive():
  
  t = Thread(target=run)
  t.start()