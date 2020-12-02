from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from window import *


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setText(text)
        self.clicked.connect(callback)

class menu(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("MAZE GAME")
        self.resize(300, 300)

        label = QLabel('      승우가 길에서 잠을 자고 있어요! \n 방향키를 이용하여 집에 데려다주세요!', self)

        font = label.font()
        font.setPointSize(20)
        label.setFont(font)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(label)
        hbox.addStretch(1)

        self.firstbutton = Button('   Level 1   ', self.buttonClicked)
        self.secondbutton = Button('   Level 2   ', self.buttonClicked)
        self.thirdbutton = Button('   Level 3   ', self.buttonClicked)
        self.forthbutton = Button('   Level 4   ', self.buttonClicked)
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.firstbutton)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.secondbutton)
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.thirdbutton)
        hbox3.addStretch(1)

        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addWidget(self.forthbutton)
        hbox4.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)
        vbox.addLayout(hbox3)
        vbox.addStretch(1)
        vbox.addLayout(hbox4)
        vbox.addStretch(1)
        self.setLayout(vbox)

    def buttonClicked(self):
        key = self.sender().text()
        if key == '   Level 1   ':
            line = 5  # 홀수
            num = 0.89
        elif key =="   Level 2   ":
            line = 21
            num = 0.56
        elif key =="   Level 3   ":
            line = 31
            num = 0.35
        else:
            line = 41
            num = 0.139
        w = CWidget(line, (line - 1) // 2, num)
        w.show()


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    calc = menu()
    calc.show()
    sys.exit(app.exec_())