from collections import defaultdict


def count(chessBoard):
    board = chessBoard.copy()
    tally = defaultdict(int)
    for (i, row) in enumerate(board):
        for (j, element) in enumerate(row):
            if i == 0 or j == 0:
                continue
            if element:
                n = board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                for x in range(n, 1, -1):
                    tally[x] += 1
    return tally
