from flask import Flask
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__, static_folder='static')
app.secret_key = 'VideoPlayer'

@app.route('/')
def video():
    return render_template("video.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
