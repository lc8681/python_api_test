# utf-8
import requests


def ign_data(pageNum):
    url = 'http://www.ign.xn--fiqs8s/article/review?platform=nintendo-switch&page=' + pageNum + '&ist=broll'
    res = requests.get(url=url)
    print(res.text)


if __name__ == '__main__':
    ign_data(str(2))
