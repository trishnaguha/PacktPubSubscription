import logging

from flask import Flask, url_for, request, render_template
from flask import redirect, flash, make_response, session
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    error = None
    #if request.method == 'POST':
    return render_template('index.html')

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

if __name__=='__main__':
    app.debug = True
    app.run()
