from collections import Counter


def connect_four_place(columns):
    board = [['-' for i in range(7)] for i in range(6)]
    c = Counter(columns)
    for (i, x) in enumerate(columns):
        board[columns.count(x) - c[x]][x] = 'YR'[i % 2]
        c[x] -= 1
    return list(reversed(board))
