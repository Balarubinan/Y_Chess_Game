# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grid_layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtGui import QIcon

from src.Mod_Button import ModButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QPushButton
from src.main import *

class Ui_Dialog(QtWidgets.QMainWindow):
    def setupUi(self, Dialog):
        self.turn=0
        self.modified=[]
        self.img = QIcon('images/King.png')
        # self.img.setIconSize(QSize(100,100))
        self.point=[]
        Dialog.setObjectName("Dialog")
        Dialog.resize(1096, 834)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 807, 807))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.chess_board = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.chess_board.setContentsMargins(0, 0, 0, 0)
        self.chess_board.setObjectName("chess_board")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add_bunch()

    def add_bunch(self):
        # button=QPushButton(self)
        # button.setStyleSheet("background-color:blue;border:1px solid dashed;")
        # button2=QPushButton(self)
        # button3 = QPushButton(self)
        # self.chess_board.addWidget(button2,1,0)
        # self.chess_board.addWidget(button3,0,0)
        # self.chess_board.addWidget(button,0,1)
        # self.chess_board.setGeometry(QRect(0,0,300,300))
        self.set_up_grid()
        self.dic={}
        dic=self.dic
        alt_style="background-color:rgb(118, 150, 85);border:none;"
        def_style = "background-color:rgb(238, 238, 210);border:none;"
        row_count=0
        for x in range(8):
            for y in range(8):
                dic[(x,y)]=ModButton(self)
                dic[(x,y)].add_x_y(int(x),int(y))
                dic[(x,y)].clicked.connect(self.called_connect(x,y))
                dic[(x,y)].setGeometry(QtCore.QRect(50, 320, 111, 101))
                dic[(x,y)].setFixedSize(100,100)
                if (row_count+y)%2==0:
                    dic[(x,y)].setStyleSheet(alt_style+"QPushButton{background: transparent;}")
                else:
                    dic[(x, y)].setStyleSheet(def_style+"QPushButton{background: transparent;}")
                self.chess_board.addWidget(dic[(x,y)],x,y)
            row_count+=1
        # dic[(4,4)].setIcon(self.img)
        self.render()
        # the below thing works as expected
        # for x in dic.values():
        #     print(x.get_x_y())

    # this syntax is called a function factory
    def called_connect(self,x, y):
        print(x, y)
        def called():
            if (len(self.point) == 0):
                self.point.append((x, y))
                self.show_possible_moves(x,y)
                print("X,y",x,y)
            elif (len(self.point) == 1):
                self.point.append((x, y))
                self.undo_selected()
                x1, y1 = self.point[0]
                x2, y2 = self.point[1]
                # Add all the chess check conditons here
                print(self.turn,self.grid,x1,y1,x2,y2)
                if validate_move(self.turn,self.grid,x1,y1,x2,y2):
                    self.update()
                    self.turn = (self.turn + 1) % 2
                else:
                    print("Wrong move!!")
                self.point = []
            # QPushButton.styleSheet()

        return called

    def update(self):
        # print(self.point)
        # p1,p2=self.point[0],self.point[1]
        # print("Fucking Update methid was called")
        # print(p1,p2)
        # self.dic[p2].setIcon(self.dic[p1].icon())
        # self.dic[p2].setIconSize(QSize(100,100))
        # self.dic[p1].setIcon(QIcon())
        x1,y1=self.point[0]
        x2,y2=self.point[1]
        print(x1,x2,y1,y2)
        self.grid[x2][y2]=self.grid[x1][y1]
        self.grid[x1][y1]='.'
        print(self.grid)
        self.check_check()
        self.render()


    def set_up_grid(self):
        self.grid=[]
        set=["R","H","B","K","Q","B","H","R"]
        self.grid.append(["B"+x for x in set])
        self.grid.append(["BP" for x in range(8)])
        for x in range(4):
            self.grid.append(['.' for x in range(8)])
        self.grid.append(["WP" for x in range(8)])
        self.grid.append(["W" + x for x in set])
        set_grid(self.grid)
        print(self.grid)

    def render(self):
        # self.grid=[list(reversed(x)) for x in self.grid]
        # self.grid.reverse()
        gr=self.grid
        for x in range(8):
            for y in range(8):
                if gr[x][y]!='.':
                    self.dic[(x,y)].setIcon(QIcon(f"images/{gr[x][y]}.png"))
                    self.dic[(x,y)].setIconSize(QSize(70, 70))
                else:
                    self.dic[(x,y)].setIcon(QIcon())

    def show_possible_moves(self,x,y):
        gr=self.grid
        for ex in range(8):
            for ey in range(8):
                if self.grid[ex][ey]=='.':
                    if movable(gr[x][y],x,y,ex,ey):
                        self.modified.append((self.dic[(ex,ey)],self.dic[(ex,ey)].styleSheet()))
                        self.dic[(ex, ey)].setStyleSheet("background-color:rgb(186, 202, 69);border:none;")
                    else:
                        self.dic[(ex, ey)].setIcon(QIcon())
            else:
                pass
    def undo_selected(self):
        for x in self.modified:
            x[0].setStyleSheet(x[1])

    def check_check(self):
        a=check()
        print(a)
        bx,by=a[1][0],a[1][1]
        wx, wy = a[2][0], a[2][1]
        if a[0][0]:
            self.dic[(bx,by)].setStyleSheet("background-color:red;border:none;")
        else:
            self.dic[(bx, by)].setStyleSheet("background-color:blue;border:none;")
        if a[0][1]:
            self.dic[(wx,wy)].setStyleSheet("background-color:red;border:none;")
        else:
            self.dic[(bx, by)].setStyleSheet("background-color:blue;border:none;")

        # self.render()



app = QtWidgets.QApplication([])
w = Ui_Dialog()
w.setupUi(w)
w.show()
import sys

sys.exit(app.exec_())
