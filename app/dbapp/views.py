from dbapp import app
from flask import render_template, request
import json
import requests
import time
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def stopno():
    stopid = request.form['stopid']
    dblink = 'http://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?stopid=' + str(stopid)+ '&format=json'
    r = requests.get(dblink)
    jsondata = json.loads(r.text)
    jsonpath = 'dbapp/static/json_data/stop' + str(stopid)+ '.json'
    dir = os.path.dirname(jsonpath)
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(jsonpath, 'w') as f:
        json.dump(jsondata, f)
    return render_template('search.html', stopid = stopid)
