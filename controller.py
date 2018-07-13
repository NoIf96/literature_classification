import algorithm
import model
import config
import shutil
from tkinter.messagebox import *
from tkinter.filedialog import *


# 分类按钮事件
def classificationButtonEvent(treeView):
    if config.texts_datas is not None:
        classifier = algorithm.TextClassifier(
            config.texts_datas.getTextsName(), config.texts_datas.getTextsSegmentationContent, config.stopwords)
        classifier.setConfig(config.k, config.max_df, config.min_df)
        config.classifier_datas = classifier.automationClassifier()
        textsClassifierTreeViewSatas(treeView)
    else:
        showerror("错误", "请先选择文本目录")


# 分类树加载函数
def textsClassifierTreeViewSatas(treeView):
    try:
        treeView.delete("分类")
    except Exception as e:
        print(e)
    finally:
        root = treeView.insert("", 0, "分类", text="分类")
        if config.classifier_datas is not None:
            for i, item in enumerate(config.classifier_datas):
                secondary_root = treeView.insert(root, i, i, text=i)
                for j, text_name in enumerate(item):
                    treeView.insert(secondary_root, j, text_name, text=text_name)
        showinfo("提示", "分类完毕")


# 目录选择按钮事件
def browseButtonEvent(treeView):
    file_dir = askdirectory()
    if file_dir != "":
        try:
            config.file_dir = file_dir
            config.texts_datas = model.TextRecorder(config.file_dir)
            textsTreeViewSatas(treeView)
        except Exception as e:
            print(e)
            showerror("错误", "请重新选择目录")


# 文本树加载事件
def textsTreeViewSatas(treeView):
    try:
        treeView.delete("文本")
    except Exception as e:
        print(e)
    finally:
        root = treeView.insert("", 0, "文本", text="文本")
        for i, text_name in enumerate(config.texts_datas.getTextsName()):
            treeView.insert(root, i, text_name, text=text_name)
        showinfo("提示", "导入完毕")


# 文件夹构造函数
def mkdir(path):
    import os
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False


# 导出按钮事件
def exportButtonEvent():
    if config.classifier_datas is not None:
        try:
            file_dir = askdirectory()
            if file_dir != "":
                file_dir += '/分类/'
                for i, item in enumerate(config.classifier_datas):
                    path = file_dir + str(i) + '/'
                    mkdir(path)
                    for file_name in item:
                        file_path = config.file_dir + '/' + file_name
                        shutil.copy(file_path, path + file_name)
                showinfo("提示", "导出完毕")
        except Exception as e:
            showerror("错误", e)
    else:
        showerror("错误", "请先选择进行分类")


# 聚类数修改按钮事件
def setKButtonEvent(k):
    config.k = k
