from flask import Flask, render_template, request,  url_for, redirect
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	conn = sqlite3.connect("tickets.db")
	c = conn.cursor()

	c.execute("SELECT bands.name, concerts.local, concerts.tickets_available FROM bands JOIN concerts ON bands.id = concerts.bands_id")
	data = c.fetchall()
	print("MINHA DATA", data)

	return render_template('index.html', data=data)

@app.route('/new', methods=['GET'])
def new():
	return render_template('band_register.html')

@app.route('/create_band', methods=['POST'])
def create_band():
	if request.method=='POST':
		conn = sqlite3.connect("tickets.db")
		c = conn.cursor()

		#bands db
		band_name = request.form['band_name']
		category = request.form['category']
		#concerts db
		# local = request.form['local']
		# date = request.form['date']
		# time = request.form['time']

		c.execute("INSERT INTO bands (name, category) VALUES (?, ?)",(band_name, category))
		#
		# c.execute("SELECT id FROM bands")
		# band_id = c.fetchall()

		# for band_id in band_id:
		# 	c.execute("INSERT INTO concerts (bands_id, local, date, time) VALUES (?, ?, ?, ?)",(band_id[0], local, date, time,))
		conn.commit()

		return redirect(url_for('list_bands'))
	else:
		return "erro"

@app.route('/list_bands', methods=['GET', 'POST'])
def list_bands():
	conn = sqlite3.connect("tickets.db")
	c = conn.cursor()
	c.execute("SELECT * FROM bands")
	data = c.fetchall()

	return render_template('list_bands.html', data=data)

@app.route('/delete_band', methods=['POST', 'DELETE'])
def delete_band():
	if request.method == "POST":
		if request.form['action'] == 'Delete':
			band_id = request.form['id']
			conn = sqlite3.connect("tickets.db")

			return render_template('list_bands.html', name=name)
	return "erro"


@app.route('/edit_band/<id>')
def edit_band(id):
	conn = sqlite3.connect("tickets.db")
	c = conn.cursor()

	c.execute("SELECT * FROM bands WHERE id = (?)", (id,))
	band = c.fetchall()

	return render_template('concert_register_update.html', band=band)

@app.route('/update_band', methods=['POST', 'DELETE'])
def update_band():
	id = request.form['id']
	band_name = request.form['band_name']
	category = request.form['category']

	conn = sqlite3.connect("tickets.db")
	c = conn.cursor()
	c.execute("UPDATE bands SET name = (?), category = (?) WHERE id = (?)", (band_name, category, id))
	conn.commit()

	return redirect(url_for('list_bands'))

app.run(debug=True)
