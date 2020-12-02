from character import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from threading import Thread, Lock
from maze import *
import os


class CMap:

    def __init__(self, parent, lin, siz, num):
        super().__init__()

        # 쓰레드(실행흐름) 생성
        self.thread = Thread(target=self.playgame)
        # 쓰레드 동기화 락
        self.lock = Lock()

        # 게임 진행 상태
        self.bGame = False

        # 맵의 줄수
        self.lines = lin

        #미로 생성
        self.Room = Room(0, 0)
        self.mazing = self.Room.makingmaze(siz)
        self.startpo = self.Room.startpoint()
        self.list = self.Room.point()

        #말 생성
        self.horse = Character(self.lines, self.startpo[1], self.startpo[0])

        # 부모 윈도우 저장
        self.parent = parent
        # 부모 윈도우 크기 저장
        self.outrect = parent.rect()
        # 내부 맵 여백 조정
        gap = 10
        self.inrect = self.outrect.adjusted(gap, gap, -gap, -gap)

        # 맵 한칸의 크기
        self.wsize = self.inrect.width() / self.lines
        self.hsize = self.inrect.height() / self.lines

        # 맵 사각형 좌표 저장
        self.left = self.inrect.left()
        self.top = self.inrect.top()
        self.right = self.inrect.right()
        self.bottom = self.inrect.bottom()

        # 맵 사각형 저장 2차원 배열 생성 [ [열] 행]
        self.rect = [[QRectF for _ in range(self.lines)] for _ in range(self.lines)]

        for i in range(self.lines):
            for j in range(self.lines):
                self.rect[i][j] = QRect(self.left + (j * self.wsize)
                                        , self.top + (i * self.hsize)
                                        , self.wsize
                                        , self.hsize)

        #사진 경로
        self.peopleimage = os.path.abspath("./mazegame/seungwoo.jpg")
        self.homeimage = os.path.abspath("./mazegame/home.png")

        #게임 단계별 사진 비율
        self.num = num


    def draw(self, qp):

        # 맵 그리기
        for i in range(self.lines + 1):
            # 가로선
            qp.drawLine(self.left, self.top + (i * self.hsize), self.right, self.top + (i * self.hsize))
            # 세로선
            qp.drawLine(self.left + (i * self.wsize), self.top, self.left + (i * self.wsize), self.bottom)

        #미로 그리기
        #검정색으로 모두 칠하기
        qp.setBrush(QColor(0, 0, 0))
        for q in range(self.lines):
            for p in range(self.lines):
                qp.drawRect(self.rect[p][q])
        #통로를 흰색으로 칠하기
        qp.setBrush(QColor(255, 255, 255))
        for i in self.mazing:
            for j in range(2):
                qp.drawRect(self.rect[i[0]][i[1]])

        #출발점 흰색으로 칠하기
        qp.drawRect(self.rect[self.startpo[0]][self.startpo[1]])

        #집 사진 위치 설정
        rect = QRect(self.wsize + self.wsize - (self.wsize * self.num), self.wsize - (self.wsize * self.num),
                      self.wsize, self.wsize)
        qp.drawPixmap(rect, QPixmap(self.homeimage))

        #사람 사진 위치 설정
        self.lock.acquire()
        for node in self.horse.node:
            rect = QRect((node.x+self.lines)*self.wsize+self.wsize-(self.wsize*self.num), node.y*self.wsize+self.wsize-(self.wsize*self.num), self.wsize, self.wsize)
            qp.drawPixmap(rect, QPixmap(self.peopleimage))
        self.lock.release()

    def keydown(self, key):

        #게임 시작, 첫턴에 진행가능한 방향 설정
        if (key == Qt.Key_Left or key == Qt.Key_Up or key == Qt.Key_Down) and self.bGame == False:
            self.bGame = True
            self.thread.start()

        #게임 진행중 이동
        if (key == Qt.Key_Left or key == Qt.Key_Right or key == Qt.Key_Up or key == Qt.Key_Down) and self.bGame == True:
            self.lock.acquire()
            self.horse.move(key, self.list)
            self.lock.release()
            self.parent.update()

        #도착 후 게임 종료
        if self.horse.node[0].x == (-1)*(self.lines-1) and self.horse.node[0].y == 0:
            self.bGame = False

    #게임 진행중
    def playgame(self):
        while self.bGame:
            self.lock.acquire()
            self.lock.release()
            self.parent.update()
        self.parent.endSignal.emit()