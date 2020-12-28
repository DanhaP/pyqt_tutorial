## Ex 3-7. 툴바 만들기.
##https://wikidocs.net/21932

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('web.png'), 'Hello', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('EEEEE')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar('honghong')
        self.toolbar.addAction(exitAction)

        self.setWindowTitle('ex-3-7')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())