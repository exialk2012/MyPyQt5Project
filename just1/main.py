import MyWindow
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow.MyWindow()
    sys.exit(app.exec_())