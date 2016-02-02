from flask import Flask, render_template, request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/udub')
def udub():
    return render_template('udub.html')

@app.route('/osu')
def osu():
    return render_template('osu.html')

if __name__ == "__main__":
    app.debug=True
    app.run()
