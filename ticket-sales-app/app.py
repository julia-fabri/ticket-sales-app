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

		#bands db
		band_name = request.form['band_name']
		category = request.form['category']
		#concerts db
		local = request.form['local']
		date = request.form['date']
		time = request.form['time']

		c.execute("INSERT INTO bands (name, category) VALUES (?, ?)",(band_name, category))

		# c.execute("INSERT INTO concerts (band_id, local, date, time) VALUES (?, ?, ?, ?)",(band_id, local, date, time,))
		conn.commit()

		c.execute("SELECT * FROM bands")
		name = c.fetchall()

		return render_template('list_concerts.html', name=name)
	else:
		return "erro"

@app.route('/list', methods=['GET', 'POST'])
def list():
	conn = sqlite3.connect("tickets.db")
	c = conn.cursor()

	c.execute("SELECT * FROM bands")
	name = c.fetchall()

	return render_template('list_concerts.html', name=name)

@app.route('/delete', methods=['POST', 'DELETE'])
def delete():
	if request.method == "POST":
		if request.form['action'] == 'Delete':
			band_id = request.form['id'] 
			conn = sqlite3.connect("tickets.db")
			c = conn.cursor()
			print(band_id)
			c.execute("DELETE FROM bands WHERE id = (?)", (band_id,))
			conn.commit()
			c.execute("SELECT * FROM bands")
			name = c.fetchall()

			return render_template('list_concerts.html', name=name) 
	return "erro"


app.run(debug=True)
