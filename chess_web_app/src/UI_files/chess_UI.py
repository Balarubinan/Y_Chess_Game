# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chess_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from UI_files.ModButton import ModButton

class Ui_Dialog(QtWidgets.QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1290, 846)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 10, 800, 800))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # self.gridLayout.setSpacing(0)
        # self.gridLayout.setVerticalSpacing(0)
        # self.gridLayout.setHorizontalSpacing(0)

        self.black = QtWidgets.QPushButton(Dialog)
        self.black.setGeometry(QtCore.QRect(50, 220, 111, 101))
        self.black.setStyleSheet("background-color:rgb(118, 150, 86);")
        self.black.setText("")
        self.black.setObjectName("black")
        self.white = QtWidgets.QPushButton(Dialog)
        self.white.setGeometry(QtCore.QRect(50, 320, 111, 101))
        self.white.setStyleSheet("background-color:rgb(238, 238, 210)")
        self.white.setText("")
        self.white.setObjectName("white")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.add_buttons_to_grid()

    def add_buttons_to_grid(self):
        style1,style2="background-color:rgb(238, 238, 210);border-style:none;","background-color:rgb(118, 150, 86);border-style:none"
        self.buttons={}
        buttons=self.buttons
        cnt=0
        # b=ModButton(self)
        # b.setText("Ehllo")
        # b.setGeometry(QtCore.QRect(50, 220, 100, 100))
        for x in range(8):
            for y in range(8):
                buttons[(x,y)]=ModButton(self)
                # buttons[(x,y)].setGeometry(QtCore.QRect(50, 220, 111, 101))
                buttons[(x,y)].set_x_y(x,y)
                buttons[(x,y)].setFixedSize(111,101)
                self.gridLayout.addWidget(buttons[(x,y)],x,y)
                if (y+cnt)%2==0:
                    buttons[(x,y)].setStyleSheet(style1)
                else:
                    buttons[(x,y)].setStyleSheet(style2)
            cnt+=1

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

app = QtWidgets.QApplication([])
w = Ui_Dialog()
w.setupUi(w)
w.show()
import sys

sys.exit(app.exec_())

