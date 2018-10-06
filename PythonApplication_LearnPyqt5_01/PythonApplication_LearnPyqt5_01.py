"""
ZetCode PyQt5 tutorial 

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com 
Last edited: August 2017
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon
from PyQt5 import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,300,320)
        self.setWindowTitle('Icon............')
        self.setWindowIcon(QIcon("C:\\Users\\crige\\source\\repos\\Learn_Pyqt5\\PythonApplication_LearnPyqt5_01\\PythonApplication_LearnPyqt5_01\\wechat.png"))
        # RL_E3E9_dic.png 这个PNG文件加载不了，可能是不识别，换了wechat.png就识别了。
        #self.setWindowFlags(Qt.Qt.CustomizeWindowHint) #去掉标题栏的代码
        self.show()

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = Example()

    w = QWidget()
    w.resize(250,150)
    w.move(600,300)
    w.setWindowTitle('Simple')
    w.setWindowTitle("The new title....")
    w.setWindowIcon(QIcon('img_0048.jpg')) #This method is run too
    w.show()
    
    sys.exit(app.exec_())

