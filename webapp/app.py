import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world! my worldddd'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
