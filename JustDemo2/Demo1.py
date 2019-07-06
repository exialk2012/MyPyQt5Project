import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QDial,QLCDNumber

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.uiInit()

    def uiInit(self):
        self.value = 0

        self.dial = QDial(self)
        self.dial.move(0,100)
        self.dial.setRange(0,9999)
        self.dial.setNotchesVisible(True)
        self.lcd = QLCDNumber(self)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('来来来')
        
        # self.dial.valueChanged.connect(self.lcd.display)

        self.show()

    def mousePressEvent(self,e):
        self.value +=1
        print(self.value)
        self.lcd.display(self.value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MyWindow()
    sys.exit(app.exec_())