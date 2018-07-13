# coding=utf-8
import pymongo
from time import time
import crawler.config as config

def saveData(datas):
    client = pymongo.MongoClient('localhost', 27017)
    db = client[config.dbname]
    tab = db['web_urls']


    for data in datas:
        tab.insert_one(data)
    client.close()

if __name__ == '__main__':
    url_prefix = config.url_prefix
    page = 0
    url_suffix = '&filter='

    t = time()
    datas = []
    for i in range(0, 10):
        url = url_prefix + str(page) + url_suffix
        print(url)
        data = {
            'index': i,
            'url': url,
        }
        datas.append(data)
        page += 25
    saveData(datas)

    print("运行结束 用时: ", time() - t)
