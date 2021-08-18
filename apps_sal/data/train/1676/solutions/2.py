
import fileinput
import sys
from collections import Counter
from math import sqrt


def get_input():
    return [line for line in fileinput.input()]


class NewGame2:
    N = 10
    map = [[0 for i2 in range(0, N)] for j2 in range(0, N)]
    score = 0
    moves = 0
    debug = False

    def __init__(self):
        pass

    def play(self, pieces):
        clear = False
        clear = True
        if self.moves > 3:
            return '-1 -1 -1 -1 -1 -1 -1 -1 -1'

        res = self.getMoves(pieces)

        placed = 0

        gameOver = False
        for i in range(0, len(res)):
            if res[i] == -1:
                gameOver = True

        if not gameOver:
            clearRows = 0
            clearColumns = 0

            for i in range(0, len(res), 3):
                p = self.defi[pieces[res[i] - 1]]
                posy = res[i + 1] - len(p)
                posx = res[i + 2] - 1

                for py in range(0, len(p)):
                    for px in range(0, len(p[0])):
                        if p[py][px] > 0:
                            self.map[posy + py][posx + px] = pieces[res[i] - 1] + 1
                            placed += 1

                rows = [False for i in range(0, self.N)]
                columns = [False for i in range(0, self.N)]

                for y in range(0, self.N):
                    fill = 0
                    for x in range(0, self.N):
                        if self.map[y][x] > 0:
                            fill += 1
                    if fill == self.N:
                        rows[y] = True
                        clearRows += 1

                for x in range(0, self.N):
                    fill = 0
                    for y in range(0, self.N):
                        if self.map[y][x] > 0:
                            fill += 1
                    if fill == self.N:
                        columns[y] = True
                        clearColumns += 1

                for y in range(0, self.N):
                    for x in range(0, self.N):
                        if (rows[y] or columns[x]) and clear:
                            self.map[y][x] = 0

            size = 0
            for y in range(0, self.N):
                for x in range(0, self.N):
                    if self.map[y][x] > 0:
                        size += 1

            if size == 0:
                self.score += 500

            self.score += placed
            self.score += clearColumns * clearColumns + clearRows * clearRows + (5 * clearRows * clearColumns)
            self.moves += 1

        output = ""
        for i in range(0, len(res)):
            if (i > 0):
                output += " "

            output += str(res[i])

        return output

    def getMoves(self, pieces):
        res = [-1 for i in range(0, 9)]
        tMap = [[0 for i2 in range(0, self.N)] for j2 in range(0, self.N)]

        for y in range(0, self.N):
            for x in range(0, self.N):
                tMap[y][x] = self.map[y][x]

        for i in range(0, len(pieces)):
            p = self.defi[pieces[i]]

            found_move = False
            for y in range(0, self.N):
                for x in range(0, self.N):
                    if not found_move:
                        valid = True
                        for py in range(0, len(p)):
                            for px in range(0, len(p[0])):
                                if valid and (y + py >= self.N or x + px >= self.N or (p[py][px] > 0 and tMap[y + py][x + px] != 0)):
                                    valid = False
                                    break
                        if (valid):
                            for py in range(0, len(p)):
                                for px in range(0, len(p[0])):
                                    if (p[py][px] > 0):
                                        tMap[y + py][x + px] = pieces[i] + 1

                            res[i * 3 + 0] = i + 1
                            res[i * 3 + 1] = y + len(p)
                            res[i * 3 + 2] = x + 1
                            found_move = True
                            break

        return res

    defi = [
        [
            [1],
        ],
        [
            [1],
            [1],
        ],
        [
            [1, 1],
        ],
        [
            [1],
            [1],
            [1],
        ],
        [
            [1, 1, 1],
        ],
        [
            [1],
            [1],
            [1],
            [1],
        ],
        [
            [1, 1, 1, 1],
        ],
        [
            [1],
            [1],
            [1],
            [1],
            [1],
        ],
        [
            [1, 1, 1, 1, 1],
        ],
        [
            [1, 1],
            [1, 1],
        ],
        [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ],
        [
            [1, 1, 1],
            [0, 0, 1],
            [0, 0, 1],
        ],
        [
            [0, 0, 1],
            [0, 0, 1],
            [1, 1, 1],
        ],
        [
            [1, 0, 0],
            [1, 0, 0],
            [1, 1, 1],
        ],
        [
            [1, 1, 1],
            [1, 0, 0],
            [1, 0, 0],
        ],
        [
            [1, 1],
            [1, 0],
        ],
        [
            [1, 1],
            [0, 1],
        ],
        [
            [0, 1],
            [1, 1],
        ],
        [
            [1, 0],
            [1, 1],
        ],
    ]


class JUNE16:
    def __init__(self):
        self.CHNWGM()

    def CHNWGM(self):
        game = NewGame2()
        while True:
            a = [int(x) - 1 for x in input().split()]
            if a[0] < 0 or a[1] < 0 or a[2] < 0:
                return
            print(game.play(a))

            sys.stdout.flush()
            sys.stdin.flush()


def __starting_point():
    JUNE16()


__starting_point()
