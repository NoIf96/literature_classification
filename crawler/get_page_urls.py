# coding=utf-8
from bs4 import BeautifulSoup
import urllib
import urllib.parse
import urllib.request
import pymongo
import crawler.config as config
from time import time

def readData():
    client = pymongo.MongoClient('localhost', 27017)
    db = client[config.dbname]
    tab = db['web_urls']
    urls = [item['url'] for item in tab.find()]
    client.close()
    return urls

def saveData(datas):
    client = pymongo.MongoClient('localhost', 27017)
    db = client[config.dbname]
    tab = db['page_urls']

    for data in datas:
        tab.insert_one(data)
    client.close()


def getPageUrl(url):
    web_data = urllib.request.urlopen(url)
    soup = BeautifulSoup(web_data, 'lxml')
    links = soup.select(config.page_select)
    hrefs = []
    for link in links:
        href = link['href']
        hrefs.append(href)
    return hrefs

if __name__ == '__main__':
    #加载网页连接数据
    web_urls = readData()
    t = time()
    #获取电影页面链接
    datas = []
    index = 0
    for web_url in web_urls:
        print(web_url)
        page_urls = getPageUrl(web_url)
        for page_url in page_urls:
            print(page_url)
            data = {
                'index': index,
                'url': page_url,
            }
            datas.append(data)
            index += 1
    #保存数据
    saveData(datas)
    print("运行结束 用时: ", time() - t)

