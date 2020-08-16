from PyQt5.QtWidgets import QPushButton

class ModButton(QPushButton):
    def add_x_y(self,x,y):
        self.x,self.y=x,y

    def get_x_y(self):
        return(self.x,self.y)

