from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from PyQt5.QtGui import QFont
import sys

app=QApplication(sys.argv)
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(700,250,500,500)
        self.setFixedSize(380, 580)
        self.start()
    def font(self,obj,x,y):
        self.setFont(QFont("Times",35))
        obj.move(x,y)
    def start(self):
        self.n0=QPushButton("0",self)
        self.font(self.n0,105,490)
        self.n0.clicked.connect(self.nol)

        self.n1=QPushButton("1",self)
        self.font(self.n1,15,250)
        self.n1.clicked.connect(self.bir)

        self.n2=QPushButton("2",self)
        self.font(self.n2,105,250)
        self.n2.clicked.connect(self.ikki)

        self.n3=QPushButton("3",self)
        self.font(self.n3,195,250)
        self.n3.clicked.connect(self.uch)

        self.n4=QPushButton("4",self)
        self.font(self.n4,15,330)
        self.n4.clicked.connect(self.tort)

        self.n5=QPushButton("5",self)
        self.font(self.n5,105,330)
        self.n5.clicked.connect(self.besh)

        self.n6=QPushButton("6",self)
        self.font(self.n6,195,330)
        self.n6.clicked.connect(self.olti)
        
        self.n7=QPushButton("7",self)
        self.font(self.n7,15,410)
        self.n7.clicked.connect(self.yetti)
        
        self.n8=QPushButton("8",self)
        self.font(self.n8,105,410)
        self.n8.clicked.connect(self.sakkiz)
        
        self.n9=QPushButton("9",self)
        self.font(self.n9,195,410)
        self.n9.clicked.connect(self.toqqiz)
        
        self.plus=QPushButton("\n+\n",self)
        self.plus.setFont(QFont("Times",19))
        self.plus.move(285,250)
        self.plus.clicked.connect(self.Plus)
        
        self.minus=QPushButton("\n-\n",self)
        self.minus.setFont(QFont("Times",20))
        self.minus.move(285,365)
        self.minus.clicked.connect(self.Minus)
        
        self.c=QPushButton("c",self)
        self.font(self.c,15,490)
        self.c.clicked.connect(self.cleaning)
        
        self.teng=QPushButton("       =     ",self)
        self.font(self.teng,195,490)
        self.teng.clicked.connect(self.Teng)
        
        self.s1=QLabel("0",self)
        self.s1.setFont(QFont("Times",20))
        self.s1.move(18,210)
    
    def bir(self):
        if self.s1.text()!='0':
            self.s1.setText(self.s1.text()+self.n1.text())
        else:
            self.s1.setText(self.n1.text())
        self.s1.adjustSize()

    def ikki(self):
        if self.s1.text()!='0':
            self.s1.setText(self.s1.text()+self.n2.text())
        else:
            self.s1.setText(self.n2.text())
        self.s1.adjustSize()

    def uch(self):
        if self.s1.text()!='0':
            self.s1.setText(self.s1.text()+self.n3.text())
        else:
            self.s1.setText(self.n3.text())
        self.s1.adjustSize()

    def tort(self):
        if self.s1.text()!='0':
            self.s1.setText(self.s1.text()+self.n4.text())
        else:
            self.s1.setText(self.n4.text())
        self.s1.adjustSize()
    
    def besh(self):
        if self.s1.text()!='0':
            self.s1.setText(self.s1.text()+self.n5.text())
        else:
            self.s1.setText(self.n5.text())
        self.s1.adjustSize()
    
    def olti(self):
        if self.s1.text()!='0':
            self.s1.setText(self.s1.text()+self.n6.text())
        else:
            self.s1.setText(self.n6.text())
        self.s1.adjustSize()
    
    def yetti(self):
        if self.s1.text()!='0':
            self.s1.setText(self.s1.text()+self.n7.text())
        else:
            self.s1.setText(self.n7.text())
        self.s1.adjustSize()
    
    def sakkiz(self):
        if self.s1.text()!='0':
            self.s1.setText(self.s1.text()+self.n8.text())
        else:
            self.s1.setText(self.n8.text())
        self.s1.adjustSize()
    
    def toqqiz(self):
        if self.s1.text()!='0':
            self.s1.setText(self.s1.text()+self.n9.text())
        else:
            self.s1.setText(self.n9.text())
        self.s1.adjustSize()
    
    def nol(self):
        if self.s1.text()!='0':
            self.s1.setText(self.s1.text()+self.n0.text())
        else:
            self.s1.setText(self.n0.text())
        self.s1.adjustSize()

    def Plus(self):
        if self.s1.text()=='0' or self.s1.text()[len(self.s1.text())-1]=='+' or self.s1.text()[len(self.s1.text())-1]=='-':
            pass
        else:
            self.s1.setText(self.s1.text()+'+')
        self.s1.adjustSize()
    
    def Minus(self):
        if self.s1.text()=='0' or self.s1.text()[len(self.s1.text())-1]=='+' or self.s1.text()[len(self.s1.text())-1]=='-':
            pass
        else:
            self.s1.setText(self.s1.text()+'-')
        self.s1.adjustSize()

    def Teng(self):
        if self.s1.text()=='0' or self.s1.text()[len(self.s1.text())-1]=='+' or self.s1.text()[len(self.s1.text())-1]=='-':
            pass
        else:
            self.s1.setText(str(eval(self.s1.text())))

    def cleaning(self):
        self.s1.setText('0')

    

oyna=window()
oyna.show()
app.exec_()