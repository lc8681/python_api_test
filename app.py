from flask import Flask, jsonify
from flask import request
from flask import redirect
from flask import jsonify
import json

app = Flask(__name__)

AD_List = [
    {
        'id': '1',
        'splash_url': 'https://img.zcool.cn/community/012de8571049406ac7251f05224c19.png@1280w_1l_2o_100sh.png',
        'splash_goto': 'https://www.sina.com.cn',
        'showCard_url': 'http://img.zcool.cn/community/01b4345732e24e6ac725263177fd29.jpg',
        'showCard_goto': 'https://www.baidu.com',
        'list_url': 'http://img.zcool.cn/community/01acaf5722af116ac7253812b32635.jpg@1280w_1l_2o_100sh.jpg',
        'list_goto': 'https://www.baidu.com',
        'code': '1000'
    }
]


@app.route('/api/ad/', methods=['GET'])
def start():
    return jsonify({'AD_List': AD_List})


if __name__ == '__main__':
    app.run(host='192.168.1.109', port=5000, debug=False)
