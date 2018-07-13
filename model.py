# -*- coding: utf-8 -*-
import jieba
import re
import os


class TextRecorder(object):
    def __init__(self, file_dir):
        self.__texts_name = self.__readTextNames(file_dir)
        self.__texts_content = self.__readTextContents(file_dir, self.__texts_name)

    @property  # 切词后文本访问器
    def getTextsSegmentationContent(self):
        return [" ".join(text_segmentation) for text_segmentation in
                [self.__segmentationText(text_content) for text_content in self.__texts_content]]

    # 文本切词函数
    def __segmentationText(self, text_content):
        return jieba.lcut(text_content)

    # 文本清洗函数 清洗无用符号
    def __cleanText(self, text_content):
        return re.sub(" +", "", text_content.replace("\n", ""))

    # 读取文本名（全部）
    def __readTextNames(self, file_dir):
        return [f for f in os.listdir(file_dir) if f.endswith('.txt')]

    # 读取文本内容（全部）
    def __readTextContents(self, file_dir, file_names):
        return [self.__cleanText(self.__readTextContent(file_path)) for file_path in
                [file_dir + "/" + file_name for file_name in file_names]]

    # 读取文本内容（个）
    def __readTextContent(self, file_path):
        with open(file_path, "r", encoding="utf-8") as fp:
            text_content = fp.read()
        return text_content

    # 文本名访问器
    def getTextsName(self):
        return self.__texts_name

    # 文本内容访问器
    def getTextsContent(self):
        return self.__texts_content


if __name__ == '__main__':
    a = TextRecorder('I:/豆瓣电影TOP250简介')
    print(a.getTextsSegmentationContent)
