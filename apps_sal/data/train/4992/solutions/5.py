from copy import copy, deepcopy


def bingo(card, numbers):
    copy = deepcopy(card)

    def checkEqual(e, x):
        for i in range(1, len(copy)):
            if copy[i][x] == int(e[1:]):
                copy[i][x] = None

    def markBoard():
        for e in numbers:
            if e[0] == 'B':
                checkEqual(e, 0)
            if e[0] == 'I':
                checkEqual(e, 1)
            elif e[0] == 'N':
                checkEqual(e, 2)
            elif e[0] == 'G':
                checkEqual(e, 3)
            elif e[0] == 'O':
                checkEqual(e, 4)

    def checkVerticle():
        for i in range(1, len(copy)):
            for j in range(len(copy) - 1):
                if copy[i][j] != None and copy[i][j] != 'FREE SPACE':
                    break
            else:
                return True
        return False

    def checkLateral():
        for i in range(len(copy) - 1):
            for j in range(1, len(copy)):
                if copy[j][i] != None and copy[j][i] != 'FREE SPACE':
                    break
            else:
                return True
        return False

    def checkCross():
        for i in range(1, len(copy)):
            if copy[i][i - 1] != None and copy[i][i - 1] != 'FREE SPACE':
                break
        else:
            return True
        for i in range(1, len(copy)):
            if copy[-i][i - 1] != None and copy[-i][i - 1] != 'FREE SPACE':
                break
        else:
            return True
        return False
    markBoard()
    t = checkVerticle() or checkLateral() or checkCross()
    return t


def printBoard(card):
    for i in range(len(card)):
        for j in range(len(card) - 1):
            print(card[i][j], '\t', end='')
        print()
