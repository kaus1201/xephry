from flask import Flask, render_template

app = Flask(__name__) # This 'app' must match the 'app' in main:app

@app.route('/')
def index():
    return render_template('index.html')