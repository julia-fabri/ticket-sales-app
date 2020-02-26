from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/register')
def register_concert():
    return render_template('concert_register.html')
