# -*- coding: utf-8 -*-
import os
from flask import Flask, jsonify
from flask import render_template
from flask import request, json
from settings import apiList, get_api_info
from queue import Queue
from watcher import init_watcher

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', req={ 'apiList' : json.dumps(apiList) } )


@app.route('/monitor', methods=['POST'])
def reserve():
    print("param json = %s" % ( request.json ))
    params = request.json
    api = get_api_info( params['svc_cd'], params['api_cd'])

    items = list()
    while( g_queue.empty() == False ):
        file, log = g_queue.get()
        if file == api['file_path']:
            items.append({'file': file, 'log': log.decode('utf-8')})
            # item = dict()
            # item['file'] = file
            # item['log'] = log.decode('utf-8')
            # items.append(item)

    # object 형태로 리턴
    response = app.response_class(
        response=json.dumps(items),
        status=200,
        mimetype='application/json'
    )
    return response

def isWindowOS():
    return os.name == 'nt'

def init( q ):
    if isWindowOS() == False:
        # AS-IS : TEST
        init_watcher("/home/ec2-user/deploy/korail-reservation/debug.log", q)
        init_watcher("/home/ec2-user/deploy/tts/tts/debug.log", q)

        # TO-BE : 실제 로그 경로
        # for svc in apiList:
        #     for api in svc["api_list"]:
        #         init_watcher(api["file_path"], q)


g_queue = Queue()
if __name__ == '__main__':
    init( g_queue )
    app.run(host='0.0.0.0', port=9002, debug=True)