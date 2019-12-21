# coding:utf-8

import urllib.request
from bs4 import BeautifulSoup
import requests


def ign_data(pageNum):
    url = 'http://www.ign.xn--fiqs8s/article/review?platform=nintendo-switch&page=' + pageNum + '&ist=broll'
    res = requests.get(url=url)
    html = BeautifulSoup(res.text, 'html.parser')
    for i in html.select('article a[href]'):
        return i

# if __name__ == '__main__':
#     print(ign_data(str(1)))
