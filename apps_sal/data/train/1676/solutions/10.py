from sys import stdin, stdout
from itertools import permutations
from random import random


def printBS(li):
    s = [str(i) for i in li]
    print(" ".join(s))


grid = [[0] * 10 for i in range(10)]
blocks = ({1: [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 2: [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 3: [[1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 4: [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 5: [[1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 6: [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 7: [[1, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 8: [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]], 9: [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 10: [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 11: [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 12: [[1, 1, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 13: [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 14: [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 15: [[1, 1, 1, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 16: [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 17: [[1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 18: [[0, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 19: [[1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]})
leftBelow = {1: (0, 0), 2: (1, 0), 3: (0, 0), 4: (2, 0), 5: (0, 0), 6: (3, 0), 7: (0, 0), 8: (4, 0), 9: (0, 0), 10: (1, 0), 11: (2, 0), 12: (2, 0), 13: (2, 0), 14: (2, 0), 15: (2, 0), 16: (1, 0), 17: (1, 0), 18: (1, 0), 19: (1, 0)}
pattern = {1: "dot", 2: "vert 2 line", 3: "hor 2 line", 4: "vert 3", 5: "hor 3", 6: "vert 4", 7: "hor 4", 8: "vert 5", 9: "hor 5", 10: "2*2", 11: "3*3", 12: " 3T3R", 13: "3R3B", 14: "3L3B", 15: "3L3T", 16: "2L2T", 17: "2R2T", 18: "2R2B", 19: "2L2B"}


def bounded(x, y):
    return 0 <= x <= 9 and 0 <= y <= 9


def adjzero(tempGrid, block, x, y):
    ones = 0
    for i in range(5):
        for j in range(5):
            if bounded(x + i, y + j) and blocks[block][i][j]:
                if bounded(x + i - 1, y + j) and (i == 0 or blocks[block][i - 1][j] == 0) and tempGrid[x + i - 1][y + j] == 0:
                    ones += 1
                if bounded(x + i, y + j - 1) and (j == 0 or blocks[block][i][j - 1] == 0) and tempGrid[x + i][y + j - 1] == 0:
                    ones += 1
                if bounded(x + i, y + j + 1) and (j == 4 or blocks[block][i][j + 1] == 0) and tempGrid[x + i][y + j + 1] == 0:
                    ones += 1
                if bounded(x + i + 1, y + j) and (i == 4 or blocks[block][i + 1][j] == 0) and tempGrid[x + i + 1][y + j] == 0:
                    ones += 1
    return ones


def adjnon(tempGrid, block, x, y):
    ones = 0
    for i in range(5):
        for j in range(5):
            if bounded(x + i, y + j) and blocks[block][i][j]:
                if bounded(x + i - 1, y + j) and (i == 0 or blocks[block][i - 1][j] == 0) and tempGrid[x + i - 1][y + j]:
                    ones += 1
                if bounded(x + i, y + j - 1) and (j == 0 or blocks[block][i][j - 1] == 0) and tempGrid[x + i][y + j - 1]:
                    ones += 1
                if bounded(x + i, y + j + 1) and (j == 4 or blocks[block][i][j + 1] == 0) and tempGrid[x + i][y + j + 1]:
                    ones += 1
                if bounded(x + i + 1, y + j) and (i == 4 or blocks[block][i + 1][j] == 0) and tempGrid[x + i + 1][y + j]:
                    ones += 1
    return ones


def boundary(tempGrid, block, x, y):
    bnd = 0
    for i in range(5):
        for j in range(5):
            if blocks[block][i][j] and (x + i + 1 == 10 or x + i - 1 == -1):
                bnd += 1
            if blocks[block][i][j] and (y + j + 1 == 10 or y + j - 1 == -1):
                bnd += 1
    return bnd


def points(block, x, y):
    tempGrid = [i[:] for i in grid]
    for i in range(min(5, 10 - x)):
        for j in range(min(5, 10 - y)):
            if blocks[block][i][j] == 1:
                tempGrid[i + x][j + y] = block
    lines = 0
    for i in range(10):
        for j in range(10):
            if tempGrid[i][j] == 0:
                break
        else:
            lines += 1
    for j in range(10):
        for i in range(10):
            if tempGrid[i][j] == 0:
                break
        else:
            lines += 1
    nearby = adjnon(tempGrid, block, x, y)
    nearholes = adjnon(tempGrid, block, x, y)
    bndcls = boundary(tempGrid, block, x, y)
    return 20.0 * lines + 0.25 * nearby + 0.5 * bndcls


def clearLine(lineNo, isRow):
    if isRow:
        for i in range(10):
            grid[lineNo][i] = 0
    else:
        for i in range(10):
            grid[i][lineNo] = 0


def placeBlock(block, x, y):
    for i in range(min(5, 10 - x)):
        for j in range(min(5, 10 - y)):
            if blocks[block][i][j] == 1:
                grid[i + x][j + y] = block


def clearFilledLines():
    horz = []
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 0:
                break
        else:
            horz.append(i)
    vertz = []
    for j in range(10):
        for i in range(10):
            if grid[i][j] == 0:
                break
        else:
            vertz.append(j)
    for i in horz:
        clearLine(i, True)
    for i in vertz:
        clearLine(i, False)


def printGrid():
    for i in range(10):
        for j in range(10):
            print("%02d" % grid[i][j], end=' ')
        print()


def checkPos(x, y, block):
    for i in range(5):
        for j in range(5):
            if blocks[block][i][j]:
                if x + i > 9 or y + j > 9:
                    return False
                if grid[i + x][j + y]:
                    return False
    return True


def findPos(block):
    pos = []
    for i in range(10):
        for j in range(10):
            if checkPos(i, j, block):
                pos.append((points(block, i, j), i, j))
    if pos:
        return max(pos)
    return (-1, -1, -1)


while True:
    a, b, c = list(map(int, stdin.readline().split()))
    if (a, b, c) == (-1, -1, -1):
        break
    li = [(a, 1), (b, 2), (c, 3)]
    perms = permutations(li)
    maxp = []
    maxv = -10
    pos = []
    for p in perms:
        tempGrid = [i[:] for i in grid]
        t1 = findPos(p[0][0])
        if t1 != (-1, -1, -1):
            placeBlock(p[0][0], t1[1], t1[2])
            clearFilledLines()
        t2 = findPos(p[1][0])
        if t2 != (-1, -1, -1):
            placeBlock(p[1][0], t2[1], t2[2])
            clearFilledLines()
        t3 = findPos(p[2][0])
        if t3 != (-1, -1, -1):
            placeBlock(p[2][0], t3[1], t3[2])
            clearFilledLines()
        if (t1[0] + t2[0] + t3[0]) > maxv:
            maxv = (t1[0] + t2[0] + t3[0])
            pos = [t1[1:], t2[1:], t3[1:]]
            maxp = p
        grid = tempGrid
    outstr = []
    count = 0
    for pi in range(len(maxp)):
        if pos[pi][0] != -1:
            i = maxp[pi]
            x = pos[pi][0]
            y = pos[pi][1]
            placeBlock(i[0], x, y)
            clearFilledLines()
            outstr.extend([i[1], x + 1 + leftBelow[i[0]][0], y + 1])
            count += 1
    for i in range(3 - count):
        outstr.extend([-1, -1, -1])
    printBS(outstr)
    stdout.flush()
