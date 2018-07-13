# -*- coding: utf-8 -*-

import controller
import config

from tkinter import *
from tkinter import ttk


class App(object):
    def __init__(self):
        self.__root = Tk()
        self.__root.title("文献分类项目")
        self.__root.geometry("600x490")
        self.__root.resizable(False, False)
        self.__frameNorth = Frame(self.__root)
        self.__frameCentral = Frame(self.__root)
        self.__frameSouth = Frame(self.__root)

        self.__creatFrameNorth()
        self.__creatFrameCentral()
        self.__creatFrameSouth()

        self.__frameNorth.pack(side=TOP, fill=BOTH)
        self.__frameCentral.pack(side=TOP, fill=BOTH, ipady=10)
        self.__frameSouth.pack(side=TOP, fill=BOTH, ipady=10)

    def __creatFrameNorth(self):
        # self.__aboutButton = Button(self.__frameNorth, text="关于").pack(side=LEFT)
        self.__okButton = Button(self.__frameNorth, text="更改",
                                 command=lambda: controller.setKButtonEvent(self.kIntVar.get())).pack(side=RIGHT,
                                                                                                      padx=5)
        self.kIntVar = IntVar(value=config.k)
        self.__kSpinbox = Spinbox(self.__frameNorth, textvariable=self.kIntVar, from_=1, to=10).pack(side=RIGHT)
        self.__kLabel = Label(self.__frameNorth, text="聚类数: ").pack(side=RIGHT)

    def __creatFrameCentral(self):
        self.__frameCentralLeft = Frame(self.__frameCentral)
        self.__frameCentralRight = Frame(self.__frameCentral)
        self.__textsLabel = Label(self.__frameCentralLeft, text="原文本树").pack(side=TOP)
        self.__textsClassifierLabel = Label(self.__frameCentralRight, text="分类树").pack(side=TOP)
        self.texts_treeView = ttk.Treeview(self.__frameCentralLeft, height=18)
        self.texts_classifier_treeView = ttk.Treeview(self.__frameCentralRight, height=18)
        self.texts_treeView.pack(side=TOP, padx=50)
        self.texts_classifier_treeView.pack(side=TOP, padx=50)
        self.__frameCentralLeft.pack(side=LEFT, fill=BOTH)
        self.__frameCentralRight.pack(side=RIGHT, fill=BOTH)

    def __creatFrameSouth(self):
        self.__browseButton = Button(self.__frameSouth, text="选择文本目录",
                                     command=lambda: controller.browseButtonEvent(
                                         self.texts_treeView)).pack(side=LEFT)
        self.__exportButton = Button(self.__frameSouth, text="导出", width=5,
                                     command=controller.exportButtonEvent).pack(side=RIGHT, ipadx=6)
        self.__classificationButton = Button(self.__frameSouth, text="分类", width=5,
                                             command=lambda: controller.classificationButtonEvent(
                                                 self.texts_classifier_treeView)).pack(side=RIGHT, ipadx=6)

    def run(self):
        self.__root.mainloop()


if __name__ == '__main__':
    a = App()
    a.run()
