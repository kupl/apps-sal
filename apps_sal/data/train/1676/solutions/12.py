from sys import stdin, stdout, exit
from random import random


def printBS(li):
    s = [str(i) for i in li]
    print(" ".join(s))


# grid defined as array 10x10 of 0's and 1's 1 means occupied
grid = [[0] * 10 for i in range(10)]
blocks = ({1: [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 2: [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 3: [[1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 4: [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 5: [[1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 6: [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 7: [[1, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 8: [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]], 9: [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 10: [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 11: [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 12: [[1, 1, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 13: [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 14: [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 15: [[1, 1, 1, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 16: [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 17: [[1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 18: [[0, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 19: [[1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]})
leftBelow = {1: (0, 0), 2: (1, 0), 3: (0, 0), 4: (2, 0), 5: (0, 0), 6: (3, 0), 7: (0, 0), 8: (4, 0), 9: (0, 0), 10: (1, 0), 11: (2, 0), 12: (2, 0), 13: (2, 0), 14: (2, 0), 15: (2, 0), 16: (1, 0), 17: (1, 0), 18: (1, 0), 19: (1, 0)}
pattern = {1: "dot", 2: "vert 2 line", 3: "hor 2 line", 4: "vert 3", 5: "hor 3", 6: "vert 4", 7: "hor 4", 8: "vert 5", 9: "hor 5", 10: "2*2", 11: "3*3", 12: " 3T3R", 13: "3R3B", 14: "3L3B", 15: "3L3T", 16: "2L2T", 17: "2R2T", 18: "2R2B", 19: "2L2B"}


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
    # check horizontal
    horz = []
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 0:
                break
        else:
            horz.append(i)
    vertz = []
    # check vertical
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
    for i in range(10):
        for j in range(10):
            if checkPos(i, j, block):
                return i, j
    return -1, -1


while True:
    a, b, c = list(map(int, stdin.readline().split()))
# print pattern[a],pattern[b],pattern[c]
    if (a, b, c) == (-1, -1, -1):
        break
    outstr = []
    x, y = findPos(a)
    count = 0
    if x == -1:
        count += 1
    else:
        outstr.extend([1, x + 1 + leftBelow[a][0], y + 1])
        placeBlock(a, x, y)
        clearFilledLines()
        # printGrid()
    x, y = findPos(b)
    if x == -1:
        count += 1
    else:
        outstr.extend([2, x + 1 + leftBelow[b][0], y + 1])
        placeBlock(b, x, y)
        clearFilledLines()
        # printGrid()
    x, y = findPos(c)
    if x == -1:
        count += 1
    else:
        outstr.extend([3, x + 1 + leftBelow[c][0], y + 1])
        placeBlock(c, x, y)
        clearFilledLines()
        # printGrid()
    # printGrid()
    for i in range(count):
        outstr.extend([-1, -1, -1])
    printBS(outstr)
    stdout.flush()
