from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    date = now.strftime("%d/%m/%Y")
    return render_template('home.html', time=time, date=date)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


