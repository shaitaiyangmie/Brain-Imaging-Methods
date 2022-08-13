import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout

class Quitapp(QMainWindow):
    def __init__(self):
        super(Quitapp, self).__init__()  # 调用父类的init方法
        self.resize(300, 200)
        self.setWindowTitle('退出')
        # 添加Button
        self.button1 = QPushButton('exit')
        # 绑定信号与槽
        self.button1.clicked.connect(self.onClick_Button)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onClick_Button(self):
        sender = self.sender()  # sender就是发射器，表示按钮
        print(sender.text() + '被按下')
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Quitapp()
    main.show()
    sys.exit(app.exec_())
