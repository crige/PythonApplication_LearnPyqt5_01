import sys
from PyQt5.QtWidgets import QWidget,QDesktopWidget,QApplication,QMessageBox#,QPushButton
#from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        #self.setGeometry(300,300,250,150)
        self.resize(250,150)
        self.center()
        self.setWindowTitle('Message Box')
        self.show()
    #'''
    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message',"Are u sure to quit?",QMessageBox.No|QMessageBox.Yes,QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    #'''
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())