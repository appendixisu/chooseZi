# !/usr/bin/python
# coding:utf-8

import random
import os
import flask
from flask import render_template, request
from flask import send_file, make_response, Response
import json
import shutil

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False

defaultPath = '/Users/wei-chilan/Documents/python/chooseZi'
# defaultPath = '/home/tooxen_llc/web'

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/signal', methods=['GET'])
def singal():
    return render_template('signal.html')

@app.route('/number', methods=['GET'])
def number():
    numOfitems = request.args.get('numOfitems')
    x = numOfitems if numOfitems is not None else 10

    path = defaultPath+'/imgs'
    list = os.listdir(path)
    if len(list) >= 10:
        random_filename = random.sample([
            x for x in list
            if os.path.isfile(os.path.join(path, x))
        ], int(x))
    else:
        random_filename = [
            x for x in list
            if os.path.isfile(os.path.join(path, x))
        ]

    t = {
        'name': random_filename,
        'lens': len(list)
    }
    return Response(json.dumps(t), mimetype='application/json')


@app.route('/img/<filename>', methods=['GET'])
def image(filename):
    path = defaultPath+'/imgs'
    # random_filename = random.choice([
    #     x for x in os.listdir(path)
    #     if os.path.isfile(os.path.join(path, x))
    # ])
    filePath = os.path.join(path, filename)
    print(filePath)
    return send_file(filePath, mimetype='image/jpg')
    
    # response = make_response(send_file(filePath, mimetype='image/jpg'))
    # response.headers['X-filename'] = random_filename.split('_')[1].split('.')[0]
    # return response


@app.route('/check/<filename>', methods=['GET'])
def check(filename):
    isRight = request.args.get('isRight')

    path = defaultPath+'/imgs'
    if isRight == '1':
        SourceFolder = os.path.join(path, filename)
        TargetFolder = defaultPath+'/right'
        shutil.move(SourceFolder, TargetFolder)
    else:
        SourceFolder = os.path.join(path, filename)
        TargetFolder = defaultPath+'/left'
        shutil.move(SourceFolder, TargetFolder)

    t = {
        'success': True
    }
    return Response(json.dumps(t), mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
