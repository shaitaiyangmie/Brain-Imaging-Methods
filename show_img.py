import sys
import cv2
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout


class Quitapp(QMainWindow):
    def __init__(self):
        super(Quitapp, self).__init__()  # 调用父类的init方法
        self.resize(300, 200)
        self.setWindowTitle('显示图片')
        # 添加Button
        self.button1 = QPushButton('裁剪图片')
        # 绑定信号与槽
        self.button1.clicked.connect(self.onClick_Button)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        # 先把button放入layout，再把layout放入窗口
        self.setCentralWidget(mainFrame)


    def onClick_Button(self):
        root = '/Users/shaotianyu01/Desktop/u=4290447868,1632913608&fm=26&fmt=auto.jpg'
        img = cv2.imread(root)
        bbox = cv2.selectROI(img, False)
        cut = img[bbox[1]:bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]]
        # cv2.imwrite('/Users/shaotianyu01/Desktop/school/gdg/cut_{}.jpg'.format('gdg'), cut)
        # print(sender.text() + '被按下')
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Quitapp()
    main.show()
    sys.exit(app.exec_())
