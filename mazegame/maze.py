import random

class Room():
    def __init__(self, r, c):
        self.r, self.c = r, c
        self.count = 0
        self.before = None
        self.crd = [(r+1, c), (r, c+1),
                     (r-1, c), (r, c-1)]
        random.shuffle(self.crd)
    def makingmaze(self, siz):
        self.checklist = []
        self.mazeSize = siz
        room = [[Room(r,c) for c in range(self.mazeSize)] for r in range(self.mazeSize)]
        self.Map = [[0 for c in range(self.mazeSize*2+1)] for r in range(self.mazeSize*2+1)]
        self.make(None, room[0][0], room, self.mazeSize)
        return self.checklist
    def make(self, before, place, room, mazeSize):
        place.before = before
        if place.before == None:
            self.Map[0][1] = 1
            self.checklist.append([0,1])
        else:
            self.Map[(place.r + 1)*2-1+(before.r - place.r)][(place.c+1)*2-1+(before.c - place.c)] = 1
            self.checklist.append([(place.r + 1)*2-1+(before.r - place.r), (place.c+1)*2-1+(before.c - place.c)])
        place.count = 1
        self.Map[(place.r + 1)*2-1][(place.c+1)*2-1] = 1
        self.checklist.append([(place.r + 1)*2-1, (place.c+1)*2-1])
        while len(place.crd) != 0:
            nr, nc = place.crd.pop()
            if nr >= 0 and nr < mazeSize and nc >= 0 and nc < mazeSize:
                if not room[nr][nc].count == 1:
                    self.make(place, room[nr][nc], room, mazeSize)
    def startpoint(self):
        while True:
            begin = random.randint(1, self.mazeSize * 2)
            if self.Map[begin][-2] == 0:
                continue
            self.Map[begin][-1] = 1
            startcoordinate = [begin, -1]
            return startcoordinate
    def point(self):
        return self.Map