from flask import Flask, render_template, request,redirect
from stadium import get_stadium
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('templates/index.html')

@app.route('/stadium/<id>')
def stadium(s_id):
    raise NotImplementedError
    stadium = get_stadium(s_id)
    return render_templatle('templates/stadium.html', data=stadium)

if __name__ == "__main__":
    app.debug=True
    app.run()
