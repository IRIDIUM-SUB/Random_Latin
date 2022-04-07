#!./flask/bin/python3
from crypt import methods
import json
from flask import Flask, abort, request, jsonify
import time
'''
test text for git
'''
app=Flask(__name__)
@app.route('/random_latin/',methods=['GET'])
def genlatin():
    return jsonify({
    "status":200,
    "timestamp":"",
    "content":"Palma non sine pulvere"
})
if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=5000, debug=True)