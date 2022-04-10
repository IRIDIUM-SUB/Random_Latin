#!./flask/bin/python3
from crypt import methods
import json
from flask import Flask, abort, request, jsonify, make_response
import time
import random
import linecache
'''
test text for git
'''
app = Flask(__name__)


def getlines(file_name):
    return sum(1 for _ in open(file_name))


def genlatin(file_name="Latin_Motto.txt"):
    times = int(time.time())
    lines = getlines(file_name)
    if lines > 0:
        lineno = random.randint(0, lines-1)
    else:
        return "Get Motto Failed. Check your source file.",-1
    return linecache.getline(file_name, lineno, module_globals=None),lines,times


def sendresponse():

    result_text = {
        "lines":0,
        "timestamp": "",
        "content": "Get Motto Failed. Check your source file."
    }
    result_text['content'],result_text['lines'],result_text['timestamp']=genlatin()
    print(result_text['content'])
    rst=make_response(result_text)
    
    rst.headers['Access-Control-Allow-Origin'] = '*'  # 处理CORS限制
    return rst, 200


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务

    app.add_url_rule('/random_latin/', view_func=sendresponse, methods=['GET'])# 绑定路由
    app.run(host="0.0.0.0", port=5000, debug=True)
