# coding:utf-8

import urllib.request
from bs4 import BeautifulSoup
import requests
import re


def ign_data(pageNum):
    final_list = []
    url = 'http://www.ign.xn--fiqs8s/article/review?platform=nintendo-switch&page=' + pageNum + '&ist=broll'
    html = requests.get(url=url)
    soup = BeautifulSoup(html.text, 'lxml')
    for i in soup.select('article'):
        dict = {}
        title = i.img['alt']
        img = "http://www.ign.中国" + i.img['src']
        score = str(re.findall(r"\d+\.?\d*", str(i.find('span')))).replace('[', '').replace(']', '').replace("'", '')
        goto_url = i.a['href']
        if score is '':
            score = '无'
        dict.update(title=title, img=img, score=score, goto_url=goto_url)
        final_list.append(dict)
    return final_list


