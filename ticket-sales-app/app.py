from flask import Flask, render_template, request,  url_for, redirect
from concerts import Concerts

app = Flask(__name__)

foofighters = Concerts(band_name='foofighters')
pearljam = Concerts(band_name='pearljam')

bands = [foofighters, pearljam]

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/new', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        bands.append(Concerts(request.form['band_name']))
        return redirect(url_for('register'))
    # if the method is GET, just return index.html
    return render_template('concert_register.html', bands=bands)

# @app.route('/data')
# def list_concerts():
#     band = request.args.get('band_name')
#     return f"You put {band}"

@app.route('/bands')
def list_bands():
    return render_template('list_concerts', bands=bands)
