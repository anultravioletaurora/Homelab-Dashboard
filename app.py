from flask import Flask, render_template

app = Flask(__name__)


# home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


# settings page
@app.route('/settings')
def settings():
    return render_template('settings.html')


if __name__ == '__main__':
    app.run(debug='true')
