#!/usr/bin/python3

from flask import Flask
from flask import request


app = Flask(__name__)
app.config["DEBUG"] = True

users = {'users': ['bob']}

@app.route('/user', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return users

    if request.method == 'POST':
        users['users'].append(request.form['user'])
        return ""
app.run()