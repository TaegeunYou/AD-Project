from PyQt5.QtCore import Qt
from map import *
from window import *


class Body:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Character():
    def __init__(self, lines, a, b):

        # 위치
        self.node = []

        # 방향 변수
        self.dir = Qt.Key_Right

        #시작 좌표
        self.node.append(Body(a, b))

    def move(self, key, a):
        self.dir = key
        head = Body(self.node[0].x, self.node[0].y)
        if self.dir == Qt.Key_Left:
            head.x -= 1
        elif self.dir == Qt.Key_Right:
            head.x += 1
        elif self.dir == Qt.Key_Up:
            head.y -= 1
        elif self.dir == Qt.Key_Down:
            head.y += 1
        self.node = [head]
        if a[self.node[0].y][self.node[0].x] == 0:
            if self.dir == Qt.Key_Left:
                head.x += 1
            elif self.dir == Qt.Key_Right:
                head.x -= 1
            elif self.dir == Qt.Key_Up:
                head.y += 1
            elif self.dir == Qt.Key_Down:
                head.y -= 1
        return True