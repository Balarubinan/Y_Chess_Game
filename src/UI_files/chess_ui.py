# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chess_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
# white: rgb(238, 238, 210)
#black: rgb(118, 150, 86)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap

from src.Mod_button import ModButton
from src.main import validate_move

class Ui_Dialog(QtWidgets.QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1263, 873)
        self.points=[]
        self.turn=0
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 60, 800, 800))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setVerticalSpacing(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.init_grid()
        self.add_buttons()

    def init_grid(self):
        grid=[(['.']*8)[:] for x in range(8)]
        arr = ['R', 'H', 'B', 'K', 'Q', 'B', 'H', 'R']
        for x in range(8):
            grid[0][x] = 'B' + arr[x]

        for x in range(8):
            grid[-1][x] = 'W' + arr[x]

        for x in range(8):
            grid[1][x] = 'BP'

        for x in range(8):
            grid[-2][x] = 'WP'

        self.grid=grid


    def render_board(self):
        for x in range(8):
            for y in range(8):
                if self.grid[x][y]!='.':
                    self.buttons[(x,y)].setIcon(QIcon(f"C:\\Users\\Balarubinan\\PycharmProjects\\chess_project\\src\\images\\{self.grid[x][y]}.png"))
                    self.buttons[(x,y)].setIconSize(QSize(100,100))
                else:
                    self.buttons[(x, y)].setIcon(QIcon())


    def add_buttons(self):
        self.buttons={}
        btn=self.buttons
        cnt=0
        for x in range(8):
            cnt+=1
            for y in range(8):
                btn[(x,y)]=ModButton(self)
                btn[(x,y)].add_x_y(int(x),int(y)) # tell to change this int(thin)
                btn[(x,y)].clicked.connect(self.called(x,y))
                self.gridLayout.addWidget(btn[(x,y)],x,y)
                btn[(x, y)].setFixedSize(100, 100)
                style1,style2="background-color:rgb(235, 236, 208);border:none;","background-color:rgb(119, 149, 86);border:none;"
                if (y+cnt)%2==0:
                    btn[(x,y)].setStyleSheet(style1)
                else:
                    btn[(x,y)].setStyleSheet(style2)
        print(self.buttons)
        self.render_board()

    def called(self,x,y):
        def clicked():
            self.updated(x,y)

        return clicked

    def updated(self,x,y):
        if len(self.points)==0:
            self.points.append((x,y))
        else:
            self.points.append((x,y))
            x1,y1=self.points[0][0],self.points[0][1]
            x2, y2 = self.points[1][0], self.points[1][1]
            res=self.check_valid()
            res=True
            self.points=[]
            if res is True:
                self.turn=(self.turn+1)%2
                self.grid[x2][y2]=self.grid[x1][y1]
                self.grid[x1][y1]='.'
                self.render_board()
            else:
                pass

    def check_valid(self):
        # points =[(1,2),(2,3)]
        x1,y1=self.points[0][0],self.points[0][1]
        x2, y2 = self.points[1][0], self.points[1][1]
        print(x1,y1,x2,y2)
        validate_move(self.grid,self.turn,x1,y1,x2,y2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

app = QtWidgets.QApplication([])
w = Ui_Dialog()
w.setupUi(w)
w.show()
import sys
sys.exit(app.exec_())

