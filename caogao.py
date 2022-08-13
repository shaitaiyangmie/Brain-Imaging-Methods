#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui
import sys
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import os
from caogao2 import Ui_MainWindow
from img_preprocess import img_cut


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))


class ControlBoard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ControlBoard, self).__init__()
        self.setupUi(self)
        self.file_dir = ''
        # 下面将输出重定向到textBrowser中
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)

        self.button1.clicked.connect(self.single_pred)
        self.button2.clicked.connect(self.preprocess)
        self.button3.clicked.connect(self.open_file)

    def outputWritten(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

    def single_pred(self):
        # running predict file
        import single_test_4classes

    def preprocess(self):
        # import img_preprocess
        img_cut(self.file_dir)

    def open_file(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "Select document", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        print('The dir of the selected picture is:', fileName, end='\n\n')
        self.file_dir = fileName


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ControlBoard()
    win.show()
    sys.exit(app.exec_())

