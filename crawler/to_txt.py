# coding=utf-8
import pandas as pd
import pymongo
import re
import crawler.config as config
from time import time

def readData():
    client = pymongo.MongoClient('localhost', 27017)
    db = client['watercress_file_Top_250']
    tab = db['item']
    items = []
    for item in tab.find():
        items.append([item['title'], item['item']])
    client.close()
    return items

if __name__ == '__main__':
    items = readData()
    items_pd = pd.DataFrame(items, columns=["标题", "简介"])
    print(items_pd)
    t = time()
    file_path_head = config.file_path_head
    for item in items_pd.values:
        #print(item[0])
        file_path = file_path_head + "/" + str(item[0]).split()[0] + ".txt"
        print(file_path)
        f = open(file_path, 'a+', encoding='utf-8')
        f.write(re.sub("  +", "    ", item[1]))
        f.close()

    print("运行结束 用时: ", time() - t)


