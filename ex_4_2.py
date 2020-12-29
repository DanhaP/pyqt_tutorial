## Ex 4-2. 박스 레이아웃.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        userLabel = QLabel('사용자님')
        
        statusLabel = QLabel('온라인')
        statusLabel.setStyleSheet("Color:green;")
        statusFont = statusLabel.font()
        statusFont.setPointSize(8)
        statusLabel.setFont(statusFont)

        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(userLabel)

        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(statusLabel)

        hbox_3 = QHBoxLayout()
        hbox_3.addStretch(1)
        hbox_3.addWidget(okButton)
        hbox_3.addWidget(cancelButton)
        hbox_3.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        vbox.addStretch(3)
        vbox.addLayout(hbox_3)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())