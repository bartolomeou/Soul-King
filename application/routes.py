from flask import Flask

app = Flask(__name__)


@app.route('/')
def hone():
    return render_template('home.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    URL = request.form['URL']
    df = extract(URL)
    ed
