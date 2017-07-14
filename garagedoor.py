# -*0 coding: utf-8 -*-


import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

HOST, PORT = "192.168.2.100", 31415 
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Example(QWidget):

    def lift(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Trying to connect to " + HOST)
            sock.connect((HOST,PORT))
            sock.sendall("click".encode())
            recieved = sock.recv(1024).decode()
            print(recieved)
        except Exception as e:
            print(e)
        finally:
            print("closing socket")
            sock.close()
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        qbtn = QPushButton('Click',self)
        qbtn.clicked.connect(self.lift)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)
         
        '''
        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)
        '''  
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))        
    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())  