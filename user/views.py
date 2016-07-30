from flask import render_template, request, redirect
from flask import url_for, session

from PacktPubSubscription import app

'''
View of the application
'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    print(request.form['email'])
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')
