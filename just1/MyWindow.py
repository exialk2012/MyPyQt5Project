from PyQt5.QtWidgets import QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.uiInit()

    def uiInit(self):
        self.setGeometry(300,300,640,480)
        self.setWindowTitle("这是我的第一个窗口")
        self.show()