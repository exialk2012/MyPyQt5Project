from PyQt5.QtWidgets import QWidget,QPushButton,QMessageBox,QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
import random

class MyWindow(QWidget):
    path = r'E:\MyPyQT5\MyPyQt5Project\JustDemo1\icon.ico'
    titlename = 'DEMO1'
    def __init__(self):
        super().__init__()
        self.uiInit()
        self.num = random.randint(1,100)

    def uiInit(self):
        #设置窗口的相关信息
        self.setWindowIcon(QIcon(self.path))
        self.setGeometry(300,300,300,220)
        self.setWindowTitle(self.titlename)

        #设置按钮相关信息
        self.qbtn = QPushButton('我猜',self)
        self.qbtn.setToolTip('<b>点击用来猜数字</b>')
        self.qbtn.clicked.connect(self.showMassageBox)
        self.qbtn.setGeometry(115, 150, 70 ,30)

        #设置editLine输入框相关信息
        self.text = QLineEdit('在这里输入数字',self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(80, 50, 150 ,30)

        #显示窗口
        self.show()

    def showMassageBox(self):
        try:
            guseenum = int(self.text.text())
        except Exception as e:
            self.text.setText('只能是数字')
            self.text.selectAll()
            self.text.setFocus()
        else:
            print(self.num)

            if guseenum>self.num:
                QMessageBox.about(self,'结果','你猜的数字太大了')
                self.text.setFocus()
            elif guseenum<self.num:
                QMessageBox.about(self,'结果','你猜的数字太小了')
                self.text.setFocus()
            else:
                QMessageBox.about(self,'结果','猜对了，进入下一轮')
                self.num = random.randint(1,100)
                self.text.clear()
                self.text.setFocus()

    def closeEvent(self,event):
        reply = QMessageBox.question(self,'确认','确认退出吗？',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()