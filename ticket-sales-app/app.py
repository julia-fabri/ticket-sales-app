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

@app.route('/new_band', methods=['GET'])
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
			c = conn.cursor()
			c.execute("DELETE FROM bands WHERE id = (?)", (band_id,))
			conn.commit()

		return redirect(url_for('list_bands'))
	return "erro"


@app.route('/edit_band/<id>')
def edit_band(id):
	conn = sqlite3.connect("tickets.db")
	c = conn.cursor()

	c.execute("SELECT * FROM bands WHERE id = (?)", (id,))
	band = c.fetchall()

	return render_template('band_register_update.html', band=band)

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


@app.route('/new_concert')
def new_concert():
	conn = sqlite3.connect("tickets.db")
	c = conn.cursor()

	c.execute("SELECT * FROM bands")
	bands = c.fetchall()
	return render_template('concert_register.html', bands=bands)

@app.route('/create_concert', methods=['POST'])
def create_concert():
	if request.method=='POST':
		conn = sqlite3.connect("tickets.db")
		c = conn.cursor()

		local = request.form['local']
		date = request.form['date']
		band_id = request.form['band_id']
		tickets = request.form['tickets_amount']

		c.execute("INSERT INTO concerts (local, date, bands_id, tickets_available) VALUES (?, ?, ?, ?)",(local, date, band_id, tickets))

		conn.commit()

		return redirect(url_for('list_concerts'))
	else:
		return "erro"

@app.route('/list_concerts', methods=['GET', 'POST'])
def list_concerts():
	conn = sqlite3.connect("tickets.db")
	c = conn.cursor()
	c.execute("SELECT concerts.id, concerts.local, concerts.tickets_available, concerts.date, bands.name FROM concerts LEFT JOIN bands ON bands.id = concerts.bands_id")
	data = c.fetchall()

	return render_template('list_concerts.html', data=data)

@app.route('/edit_concert/<id>')
def edit_concert(id):
	conn = sqlite3.connect("tickets.db")
	c = conn.cursor()

	c.execute("SELECT concerts.id, concerts.local, concerts.tickets_available, concerts.date, bands.name FROM concerts LEFT JOIN bands ON bands.id = concerts.bands_id WHERE concerts.id = (?)", (id,))
	concert = c.fetchall()

	return render_template('concert_register_update.html', concert=concert)


@app.route('/update_concert', methods=['POST', 'DELETE'])
def update_concert():
	id = request.form['id']
	local = request.form['local']
	tickets = request.form['tickets_amount']
	date = request.form['date']

	conn = sqlite3.connect("tickets.db")
	c = conn.cursor()

	c.execute("UPDATE concerts SET local = (?), tickets_available = (?), date = (?) WHERE id = (?)", (local, tickets, date, id))
	conn.commit()

	return redirect(url_for('list_concerts'))

@app.route('/delete_concert', methods=['POST', 'DELETE'])
def delete_concert():
	if request.method == "POST":
		if request.form['action'] == 'Delete':
			concert_id = request.form['id']
			conn = sqlite3.connect("tickets.db")
			c = conn.cursor()
			c.execute("DELETE FROM concerts WHERE id = (?)", (concert_id,))
			conn.commit()

		return redirect(url_for('list_concerts'))
	return "erro"



app.run(debug=True)
