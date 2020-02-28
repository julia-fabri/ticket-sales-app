from flask import Flask, render_template, request,  url_for, redirect
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/new', methods=['GET'])
def new():
	return render_template('concert_register.html')

@app.route('/create', methods=['POST'])
def create():
	if request.method=='POST':
		conn = sqlite3.connect("tickets.db")
		c = conn.cursor()
		name = request.form['band_name']
		print(name)
		c.execute("INSERT INTO bands (name) VALUES (?)",(name,))
		conn.commit()
		print("inserted")
		return "ok"
	else:
		return "não"

@app.route('/list', methods=['GET', 'POST'])
def list():
	name = request.form['band_name']
	print(name)
	band = Concerts(name)
	concerts.append(band)

	return render_template('list_concerts.html', concerts=concerts)

# @app.route('/data')
# def list_concerts():
#     band = request.args.get('band_name')
#     return f"You put {band}"

@app.route('/concerts/', methods=['GET', 'POST'])
def show():
	return render_template('list_concerts.html', concerts=concerts)


app.run(debug=True)
