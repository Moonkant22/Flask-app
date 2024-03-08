from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Congratulation! You deployed your flask application using Docker'

@app.route('/health')
def health():
    return 'Server is up and running'
