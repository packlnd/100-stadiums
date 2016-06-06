from flask import Flask, render_template, request,redirect
import os
import stadium

app = Flask(__name__)
stadiums = stadium.get_all_stadiums()

@app.route('/')
def index():
    return render_template('index.html', data=stadiums)

@app.route('/stadium/<id>')
def stadium(s_id):
    return render_templatle('stadium.html', data=stadiums[s_id])

if __name__ == "__main__":
    app.debug=True
    app.run()
