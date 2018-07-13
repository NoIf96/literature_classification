# coding=utf-8
from bs4 import BeautifulSoup
import requests
import pymongo
import time
import crawler.config as config

def readData():
    client = pymongo.MongoClient('localhost', 27017)
    db = client[config.dbname]
    tab = db['page_urls']
    urls = []
    for item in tab.find():
        urls.append(item['url'])
    client.close()
    return urls

def saveData(datas):
    client = pymongo.MongoClient('localhost', 27017)
    db = client[config.dbname]
    tab = db['item']

    for data in datas:
        tab.insert_one(data)
    client.close()

def getPageData(url):
    web_data = requests.get(url, headers=config.headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    index = soup.select('#content > div.top250 > span.top250-no')[0].text

    title = soup.select('#content > h1 > span')[0].text
    try:
        item = soup.select('#link-report > span.all.hidden')[0].text
    except:
        item = soup.select('#link-report > span')[0].text
    data = {
        'index': index,
        'title': title,
        'item': item.replace(u'\u3000', u'')
    }
    return data

if __name__ == '__main__':
    page_urls = readData()

    t = time.time()
    datas = []
    for page_url in page_urls:
        try:
            print(page_url)
            data = getPageData(page_url)
            print(data)
            datas.append(data)
            time.sleep(2)
        except:
            continue
    saveData(datas)

    print("运行结束 用时: ", time.time() - t)
