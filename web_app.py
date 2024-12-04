#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/zqc')
def zqc():
    return render_template('zqc.html')

@app.route('/zzx')
def zzx():
    return render_template('zzx.html')

@app.route('/fs')
def fs():
    return render_template('fs.html')

@app.route('/zy')
def zy():
    return render_template('zy.html')

if __name__ == '__main__':
    app.run(debug=True)