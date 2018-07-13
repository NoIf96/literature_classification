# -*- coding: utf-8 -*-

file_dir = 'F:\代码\python\文献分类项目\data\豆瓣电影TOP250简介'
texts_datas = None
classifier_datas = None

k = 8
max_df = 0.2
min_df = 2

stopwords = [line.strip() for line in open('stopword/stopwordDict.txt', 'r').readlines()]
