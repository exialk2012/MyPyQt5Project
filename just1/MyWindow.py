from PyQt5.QtWidgets import QWidget,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyWindow(QWidget):
    path = r'E:\MyPyQT5\MyPyQt5Project\just1\icon.ico'
    titlename = '这是我的小软件'
    def __init__(self):
        super().__init__()
        self.uiInit()

    def uiInit(self):
        #设置窗口的相关信息
        self.setWindowIcon(QIcon(self.path))
        self.setGeometry(300,300,640,480)
        self.setWindowTitle(self.titlename)

        #设置按钮相关信息
        qbtn = QPushButton('退出',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setGeometry(640/2-70/2,480/2-30/2,70,30)

        #显示窗口
        self.show()