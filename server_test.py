from flask import Flask

app = Flask(__name__)

@app.route('/')
def testing_world():
    return("Selamat datang di Flask!")