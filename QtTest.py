import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800,600)
        self.center()
        # 可以用self.setGeometry()代替
        self.setWindowTitle('mwq')   # 标题
        self.setWindowIcon(QIcon('e:\\Users\\Pictures\\mwq.jpg'))  # 图标

        # 菜单栏
        menu_control = self.menuBar().addMenu('菜单')
        act_quit=menu_control.addAction('quit')
        act_quit.triggered.connect(self.close)

        menu_help = self.menuBar().addMenu('帮助')
        act_about = menu_help.addAction('about....')
        act_about.triggered.connect(self.about)
        act_aboutqt=menu_help.addAction('aboutqt')
        act_aboutqt.triggered.connect(self.aboutqt)

        #状态栏
        self.statusBar().showMessage('程序已就绪（>_<）....')  # 左下角显示一段文字
        self.show()

    def about(self):
        QMessageBox.about(self,"about this software","什么都没有")

    def aboutqt(self):
        QMessageBox.aboutQt(self)

    #重写closeEvent
    def closeEvent(self, ev):
        reply = QMessageBox.question(self, '信息', '你确定要退出（TAT）?',
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            ev.accept()
        else:
            ev.ignore()

    #将窗口居中
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

myapp = QApplication(sys.argv)
mainwindow=MainWindow()

sys.exit(myapp.exec_()) #退出