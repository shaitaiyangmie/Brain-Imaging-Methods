# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ControlBoard.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
# utils, base_class
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("鉴别工具")
        MainWindow.resize(650, 500)

        self.browser_v_layout = QVBoxLayout()
        self.browser_label = QLabel('\n               Output', self)
        self.browser_label.setAlignment(Qt.AlignLeft)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)  # 显示框
        self.textBrowser.setGeometry(QtCore.QRect(50, 50, 550, 300))
        self.textBrowser.setObjectName("textBrowser")
        # self.browser_v_layout.addWidget(QLabel('Output', self))

        self.button1 = QtWidgets.QPushButton("Predict", self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(450, 400, 150, 30))  # (x, y, 宽, 高)
        # self.pushButton.setObjectName("开始预测")
        self.button2 = QtWidgets.QPushButton("Cut the picture", self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(250, 400, 150, 30))
        # self.button2.setObjectName("图片裁剪")
        self.button3 = QtWidgets.QPushButton("Documents", self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(50, 400, 150, 30))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 添加文件选择功能
        self.menubar2 = QtWidgets.QMenuBar(MainWindow)
        self.menubar2.setGeometry(QtCore.QRect(100, 390, 93, 28))
        self.menubar2.setObjectName("menubar2")
        self.menufile = QtWidgets.QMenu(self.menubar2)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.actionfileopen = QtWidgets.QAction(MainWindow)
        # self.actionfileopen.setGeometry(QtCore.QRect(400, 390, 93, 28))
        self.actionfileopen.setObjectName("actionfileopen")
        self.menufile.addAction(self.actionfileopen)
        self.menubar.addAction(self.menufile.menuAction())

        # 添加文件选择功能

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TDLs and brain tumor AI identification tool"))
        self.button1.setText(_translate("MainWindow", "Start prediction"))
        self.menufile.setTitle(_translate("MainWindow", "Document"))
        self.actionfileopen.setText(_translate("MainWindow", "Select document"))



