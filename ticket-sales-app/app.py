from flask import Flask, render_template, request,  url_for, redirect
from concerts import Concerts

app = Flask(__name__)

foofighters = Concerts(band_name='foofighters')
pearljam = Concerts(band_name='pearljam')

concerts = [foofighters, pearljam]

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/new', methods=['GET', 'POST'])
def new():
	return render_template('concert_register.html')

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
