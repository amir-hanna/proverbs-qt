# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 't.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(517, 256)
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle("Proverbs")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAccessibleName("")
        self.centralwidget.setAccessibleDescription("")
        self.centralwidget.setObjectName("centralwidget")
        self.button_prev = QtWidgets.QPushButton(self.centralwidget)
        self.button_prev.setGeometry(QtCore.QRect(10, 220, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.button_prev.setFont(font)
        self.button_prev.setAccessibleName("")
        self.button_prev.setAccessibleDescription("")
        self.button_prev.setText("Previous")
        self.button_prev.setObjectName("button_prev")
        self.button_next = QtWidgets.QPushButton(self.centralwidget)
        self.button_next.setGeometry(QtCore.QRect(390, 220, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.button_next.setFont(font)
        self.button_next.setAccessibleName("")
        self.button_next.setAccessibleDescription("")
        self.button_next.setText("Next")
        self.button_next.setObjectName("button_next")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 9, 501, 201))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAccessibleName("")
        self.label.setAccessibleDescription("")
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: #ffffcc")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setText("TextLabel")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

