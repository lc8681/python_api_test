# coding:utf-8

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
        img = "http://www.ign.xn--fiqs8s" + i.img['src']
        score = str(re.findall(r"\d+\.?\d*", str(i.find('span')))).replace('[', '').replace(']', '').replace("'", '')
        goto_url = str(i.a['href']).replace('www.ign.中国', 'www.ign.xn--fiqs8s')
        if score is '':
            score = '无'
        dict.update(title=title, img=img, score=score, goto_url=goto_url)
        final_list.append(dict)
    return final_list


