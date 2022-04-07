#!./flask/bin/python3
from crypt import methods
import json
from flask import Flask, abort, request,jsonify,make_response
import time
'''
test text for git
'''
app=Flask(__name__)
@app.route('/random_latin/',methods=['GET'])
def genlatin():
    result_text=jsonify({
    "status":200,
    "timestamp":"",
    "content":"Palma non sine pulvere."
})
    rst = make_response(result_text)
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst,201
if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=5000, debug=True)