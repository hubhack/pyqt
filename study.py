'''
import sys
from PyQt5.QtWidgets import QApplication,QWidget
if __name__ == "__main__":

    app  = QApplication(sys.argv)


    w = QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle ('简单')
    w.show()
    sys.exit(app.exec_())'''
import sys
from PyQt5.QtWidgets import  QMainWindow,QApplication

class Exampel(QMainWindow):

    def __init__(self):
        supper().__init__()



        self.initUI()

    def intiUI(self):
        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)   
    ex = Example()
    sys.exit(app.exec_())