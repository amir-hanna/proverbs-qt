#!/usr/bin/python3

from p_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from enum import Enum, unique
import random_quote

@unique
class Direction(Enum):
    RANDOM = 0
    NEXT = 1
    PREVIOUS = 2

class Main_Window(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.label.setText(self.get_verse(Direction.RANDOM))
        self.button_prev.clicked.connect(lambda: self.label.setText(self.get_verse(Direction.PREVIOUS)))
        self.button_next.clicked.connect(lambda: self.label.setText(self.get_verse(Direction.NEXT)))
        self.center()

    def center(self):
        qr = MainWindow.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())

    def get_verse(self, direction):
        if direction == Direction.RANDOM:
            self.quote_list, self.cur_pos = random_quote.quote_list('/home/amir/Documents/proverbs.json', 'fef08fec8be3919359bb0780c0e3320d37f49997f6dcd3e2cbf54ecc45a8c912eec80abcec9f394a295b0b16889bfbe2a90a2ca6530ab3a79a45c222168a46d9')
            return self.quote_list[self.cur_pos]
        elif direction == Direction.PREVIOUS and self.cur_pos > 0:
            self.cur_pos -= 1
            return self.quote_list[self.cur_pos]
        elif direction == Direction.NEXT and self.cur_pos < len(self.quote_list) - 1:
            self.cur_pos += 1
            return self.quote_list[self.cur_pos]
        else:
            return self.label.text()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main_Window(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



