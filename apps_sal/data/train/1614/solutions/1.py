from itertools import count, takewhile
(X, Y, HALF_DIRS) = (6, 7, ((0, 1), (1, 0), (1, 1), (1, -1)))


def who_is_winner(lstMoves):

    def isWinner():
        return any((countAligned(*dirs) >= 4 for dirs in HALF_DIRS))

    def isInsideAndSameGuy(a, b):
        return 0 <= a < X and 0 <= b < Y and (board[a][b] == who)

    def countAligned(dx, dy):
        return 1 + sum((sum(takewhile(bool, (isInsideAndSameGuy(x + dx * swap * n, y + dy * swap * n) for n in count(1)))) for swap in (1, -1)))
    board = [[' '] * Y for _ in range(X)]
    xIdx = [0] * Y
    for move in lstMoves:
        (y, who) = (ord(move[0]) - 65, move[2])
        x = xIdx[y]
        board[x][y] = who
        xIdx[y] += 1
        if isWinner():
            return move[2:]
    else:
        return 'Draw'
