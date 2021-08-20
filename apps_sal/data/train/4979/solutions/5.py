def count_deaf_rats(board):
    (o, p) = next(([i, j] for (i, l) in enumerate(board) for (j, k) in enumerate(l) if board[i][j] == 'P'))

    def distance(x, y):
        return ((o - x) ** 2 + (p - y) ** 2) ** 0.5
    d = {'←': (0, -1), '↑': (-1, 0), '→': (0, 1), '↓': (1, 0), '↖': (-1, -1), '↗': (-1, 1), '↘': (1, 1), '↙': (1, -1)}
    return sum((distance(i + d[l][0], k + d[l][1]) > distance(i, k) for (i, j) in enumerate(board) for (k, l) in enumerate(j) if l in '←↑→↓↖↗↘↙'))
