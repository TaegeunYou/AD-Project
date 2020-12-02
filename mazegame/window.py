from map import *
from PyQt5.QtWidgets import QWidget, QMessageBox


class CWidget(QWidget):
    # 시그널 생성
    endSignal = pyqtSignal()

    def __init__(self, lin, siz, num):
        super().__init__()
        self.lin = lin
        self.siz = siz
        self.num = num
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('MAZE GAME')
        self.setFixedSize(self.rect().size())

        self.map = CMap(self, self.lin, self.siz, self.num)

        self.endSignal.connect(self.ExitGame)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.map.draw(qp)
        qp.end()

    def keyPressEvent(self, e):
        self.map.keydown(e.key())

    def ExitGame(self):
        result = QMessageBox.about(self, "성공", "승우가 무사히 집에 도착했어요!       \n               감사합니다~")
        self.close()