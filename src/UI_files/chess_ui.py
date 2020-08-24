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
from PyQt5.QtWidgets import QPushButton

from src.Mod_button import ModButton
from src.main import validate_move,check,check_mate,movable,set_grid

class Ui_Dialog(QtWidgets.QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1263, 873)
        self.points=[]
        self.BKStyle,self.WKStyle=None,None
        self.turn=0
        self.modified=[]
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
                    self.buttons[(x,y)].setIconSize(QSize(70,70))
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
            set_grid(self.grid)
            self.show_possible_moves(x,y)
        else:
            self.undo_selected()
            self.points.append((x,y))
            x1,y1=self.points[0][0],self.points[0][1]
            x2, y2 = self.points[1][0], self.points[1][1]
            res=self.check_valid()
            # res=True
            self.points=[]
            print("Res valuse is",res)
            if res is True:
                self.turn=(self.turn+1)%2
                self.grid[x2][y2]=self.grid[x1][y1]
                self.grid[x1][y1]='.'
                self.checker()
                self.render_board()
            else:
                print("Wrong move!!")


    def check_valid(self):
        # points =[(1,2),(2,3)]
        x1,y1=self.points[0][0],self.points[0][1]
        x2, y2 = self.points[1][0], self.points[1][1]
        print(x1,y1,x2,y2)
        res=validate_move(self.grid,self.turn,x1,y1,x2,y2)
        print("res is ",res)
        return res

    def checker(self):
        a=check()
        self.king_coord=a[0],a[1]
        wx,wy=a[0]
        bx,by=a[1]
        Wc,Bc=a[2],a[3]
        print("Check Value is ",Wc,Bc)
        if Wc:
            self.WKStyle=self.buttons[(wx,wy)].styleSheet()
            self.buttons[(wx,wy)].setStyleSheet('background-color:red;border:none;')
        else:
            if self.WKStyle is not None:
                self.buttons[(wx,wy)].setStyleSheet(self.WKStyle)
        if Bc:
            self.BKStyle = self.buttons[(wx, wy)].styleSheet()
            self.buttons[(bx, by)].setStyleSheet('background-color:red;border:none;')
        else:
            if self.BKStyle is not None:
                self.buttons[(wx,wy)].setStyleSheet(self.BKStyle)
        # a=check_mate()
        # if a[0]:
        #     if a[1]=='B':
        #         self.buttons[(bx,by)].setStyleSheet("background-color:orange;border:none;")
        #     else:
        #         self.buttons[(wx, wy)].setStyleSheet("background-color:orange;border:none;")

    def show_possible_moves(self, x, y):
        gr = self.grid
        for ex in range(8):
            for ey in range(8):
                if self.grid[ex][ey] == '.':
                    if movable(gr[x][y], x, y, ex, ey):
                        self.modified.append((self.buttons[(ex, ey)], self.buttons[(ex, ey)].styleSheet()))
                        self.buttons[(ex, ey)].setStyleSheet("background-color:rgb(186, 202, 69);border:none;")
                    else:
                        self.buttons[(ex, ey)].setIcon(QIcon())

    def undo_selected(self):
        for x in self.modified:
            x[0].setStyleSheet(x[1])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

app = QtWidgets.QApplication([])
w = Ui_Dialog()
w.setupUi(w)
w.show()
import sys
sys.exit(app.exec_())

