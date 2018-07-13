# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from model import TextRecorder


# 文本分类算法
class TextClassifier(object):
    def __init__(self, texts_name, texts_content, stopwords_list):
        self.__texts_name = texts_name
        self.__texts_content = texts_content
        self.__stopwords = stopwords_list
        self.__vectorizer = None
        self.__kmeans_model = None
        # config
        self.__k = None
        self.__max_df = None
        self.__min_df = None
        self.defaultConfig()

    @property  # 获取TDM
    def getTDM(self):
        return self.__vectorizer.fit_transform(self.__texts_content)

    @property  # 获取聚类标签
    def getLabels(self):
        return self.__kmeans_model.labels_

    @property  # 获取分类后文本列表
    def getClassifier(self):
        # 依据聚类标签将文本名列表进行分组
        classifiers = [[] for i in range(0, self.__k)]
        for x, item in enumerate(self.__texts_name):
            classifiers[self.getLabels[x]].append(item)
        return classifiers

    # 自动文本分类处理
    def automationClassifier(self):
        self.generateTF_IDF()
        self.generateModel()
        return self.getClassifier

    # TF_IDF默写构建
    def generateTF_IDF(self):
        self.__vectorizer = TfidfVectorizer(max_features=200000, stop_words=self.__stopwords, sublinear_tf=True,
                                            max_df=self.__max_df, min_df=self.__min_df)

    # k聚类模型构建
    def generateModel(self):
        self.__kmeans_model = KMeans(n_clusters=self.__k, max_iter=600).fit(self.getTDM)  # KMeans聚类模型

    # 默认聚类值等属性设置
    def defaultConfig(self):
        self.__k = 8
        self.__max_df = 0.2
        self.__min_df = 2

    # 属性值修改器
    def setConfig(self, k, max_df, min_df):
        self.__k = k
        self.__max_df = max_df
        self.__min_df = min_df

    # 聚类数修改器
    def setK(self, k):
        self.__k = k

    # 聚类数访问器
    def getK(self):
        return self.__k

    # Max_df访问器
    def getMax_df(self):
        return self.__max_df

    # Mix_df访问器
    def getMix_df(self):
        return self.__min_df

    # Vectorizer访问器
    def getVectorizer(self):
        return self.__vectorizer

    # k聚类模型访问器
    def getKmeansModel(self):
        return self.__kmeans_model


if __name__ == '__main__':
    a = TextRecorder('I:/豆瓣电影TOP250简介')
    print(a.getTextsSegmentationContent)
    stopwords = [line.strip() for line in open('stopword/stopwordDict.txt', 'r').readlines()]
    b = TextClassifier(a.getTextsName(), a.getTextsSegmentationContent, stopwords)
    c = b.automationClassifier()
    for i in c:
        print(i)
        print("\n\n\n")
