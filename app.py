from flask import Flask, jsonify
from flask import request
from flask import redirect
from flask import jsonify
import json
from ign_spider import ign_data

app = Flask(__name__)

AD_List = {
    'code': '200',
    'data': [

        {

            'id': '1',
            'splash_url': 'https://img.zcool.cn/community/012de8571049406ac7251f05224c19.png@1280w_1l_2o_100sh.png',
            'splash_goto': 'https://www.sina.com.cn',
            'showCard_url': 'http://img.zcool.cn/community/01b4345732e24e6ac725263177fd29.jpg',
            'showCard_goto': 'https://www.baidu.com',
            'card_index': 3,
            'list_url': 'http://img.zcool.cn/community/01acaf5722af116ac7253812b32635.jpg@1280w_1l_2o_100sh.jpg',
            'list_goto': 'https://www.baidu.com',
        },
        {
            'id': '1',
            'splash_url': 'https://img.zcool.cn/community/012de8571049406ac7251f05224c19.png@1280w_1l_2o_100sh.png',
            'splash_goto': 'https://www.sina.com.cn',
            'showCard_url': 'http://img.zcool.cn/community/01b4345732e24e6ac725263177fd29.jpg',
            'showCard_goto': 'https://www.baidu.com',
            'card_index': 3,
            'list_url': 'http://img.zcool.cn/community/01acaf5722af116ac7253812b32635.jpg@1280w_1l_2o_100sh.jpg',
            'list_goto': 'https://www.baidu.com',
        },

    ]

}

Upgrade_Data = [
    {
        'show_update': True,
        'must_update': False,
        'update_url': 'http://dldir1.qq.com/weixin/android/weixin704android1420.apk',
        'update_message': "1、床前明月光\n2、疑似地上霜\n3、举头望明月\n4、低头思故乡",
        'code': '200'
    }
]

ign_data_list = {
    'code': '200',
    'data': [
        {

            'id': '1',
            'splash_url': 'https://img.zcool.cn/community/012de8571049406ac7251f05224c19.png@1280w_1l_2o_100sh.png',
            'splash_goto': 'https://www.sina.com.cn',
            'showCard_url': 'http://img.zcool.cn/community/01b4345732e24e6ac725263177fd29.jpg',
            'showCard_goto': 'https://www.baidu.com',
            'card_index': 3,
            'list_url': 'http://img.zcool.cn/community/01acaf5722af116ac7253812b32635.jpg@1280w_1l_2o_100sh.jpg',
            'list_goto': 'https://www.baidu.com',
        },
        {
            'id': '1',
            'splash_url': 'https://img.zcool.cn/community/012de8571049406ac7251f05224c19.png@1280w_1l_2o_100sh.png',
            'splash_goto': 'https://www.sina.com.cn',
            'showCard_url': 'http://img.zcool.cn/community/01b4345732e24e6ac725263177fd29.jpg',
            'showCard_goto': 'https://www.baidu.com',
            'card_index': 3,
            'list_url': 'http://img.zcool.cn/community/01acaf5722af116ac7253812b32635.jpg@1280w_1l_2o_100sh.jpg',
            'list_goto': str(ign_data(str(1))),
        },

    ]

}


@app.route('/api/ad/', methods=['GET'])
def start_ad():
    return jsonify(AD_List)


@app.route('/api/update/', methods=['GET'])
def start_update():
    return jsonify(Upgrade_Data)


@app.route('/data/ign/', methods=['GET'])
def start_spider_for_ign():
    return jsonify(ign_data_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
