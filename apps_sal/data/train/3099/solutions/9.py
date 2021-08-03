columns = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def parseMove(move):
    (loc, player) = move.split("_")
    return (columns.index(loc), player)


def placeMove(move, board):
    (loc, player) = parseMove(move)
    board[loc].append(player)


def isConnect(loc, dir, connect, board):
    count = 1
    (x, y) = loc
    player = board[x][y]

    s = 1
    isCheckForward = True
    isCheckBack = True

    while count < connect and (isCheckForward or isCheckBack):
        (sx, sy) = tuple(e * s for e in dir)

        if (isCheckForward and
            x + sx < len(board) and x + sx >= 0 and
            y + sy < len(board[x + sx]) and y + sy >= 0 and
                board[x + sx][y + sy] == player):
            count += 1
        else:
            isCheckForward = False

        if (isCheckBack and
            x - sx >= 0 and x - sx < len(board) and
            y - sy >= 0 and y - sy < len(board[x - sx]) and
                board[x - sx][y - sy] == player):
            count += 1
        else:
            isCheckBack = False

        s += 1

    return count >= connect


def findWinner(move, connect, board):
    (x, player) = parseMove(move)
    y = len(board[x]) - 1
    loc = (x, y)

    for d in [(1, 0), (0, 1), (1, 1), (1, -1)]:
        if isConnect(loc, d, connect, board):
            return player

    return None


def whoIsWinner(moves, connect, size):
    board = [[] for _ in range(size)]
    winner = None

    while not winner and len(moves) > 0:
        move = moves.pop(0)
        placeMove(move, board)
        winner = findWinner(move, connect, board)

    return winner if winner else "Draw"
