import requests
import shutil

from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='images')

STYLES = ['la_muse','rain_princess','the_scream','the_shipwreck_of_the_minotaur','udnie','wave']


@app.route('/')
def home():
    return render_template('home.html', my_string='yeah')

@app.route('/<project_id>/<style_id>')
def generate_art(project_id, style_id):
    url = 'https://www.floydlabs.com/expose/PLpMoND7crRQcFD2fPpLUc'
    files = {
        'file': open('./images/{0}/taipei101.jpg'.format(project_id)),
    }
    data = {
        'checkpoint': STYLES[int(style_id)] + '.ckpt'
    }
    path = './images/{0}/output.jpg'.format(project_id)
    r = requests.post(url, files=files, data=data, stream=True)

    if r.status_code == 200:
        with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

    return render_template('result.html', url=url_for('static', filename=project_id + '/output.jpg'))
