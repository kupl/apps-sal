from math import isclose

adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
knight = [(1, -2), (1, 2), (2, -1), (2, 1), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
def distance(x1, y1, x2, y2): return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5


def is_diagonal(a, b, i, j): return abs(a - i) == abs(b - j)
def is_ok(a, b): return 0 <= a < 8 and 0 <= b < 8


def amazon_check_mate(king, amazon):

    board = [['-' for _ in range(8)] for _ in range(8)]

    king = (8 - int(king[1]), 'abcdefgh'.index(king[0]))
    amazon = (8 - int(amazon[1]), 'abcdefgh'.index(amazon[0]))

    board[king[0]][king[1]] = 'K'
    board[amazon[0]][amazon[1]] = 'A'

    def get_adjacents(i, j, s=0): return [[board[i + k][j + l], (i + k, j + l)][s] for k, l in adjacents if is_ok(i + k, j + l)]

    def assign_check():
        for i in range(8):
            for j in range(8):
                if board[i][j] == '-' and (i == amazon[0] or j == amazon[1] or is_diagonal(*amazon, i, j)) and \
                        not isclose(distance(*amazon, *king) + distance(*king, i, j), distance(*amazon, i, j), abs_tol=10e-5):
                    board[i][j] = '
        for i, j in knight:
            ni, nj = amazon[0] + i, amazon[1] + j
            if is_ok(ni, nj) and board[ni][nj] != 'K':
                board[ni][nj] = '

    def assign_king_check():
        for i, j in adjacents:
            ni, nj = king[0] + i, king[1] + j
            if is_ok(ni, nj) and board[ni][nj] != 'A':
                board[ni][nj] = '$'

    def assign_checkmates():
        exceptions = set(get_adjacents(*amazon, 1))
        for i in range(8):
            for j in range(8):
                if board[i][j] == '
                    board[i][j] = '*'

    def king_amazon_adj():
        adj = get_adjacents(*amazon)
        return adj.count('

    def assign_safe_not_safe():
        for i in range(8):
            for j in range(8):
                if board[i][j] == '-' and all(n != '-' for n in get_adjacents(i, j)):
                    board[i][j]='@'

    def _count():
        assign_check()
        assign_king_check()
        assign_checkmates()
        assign_safe_not_safe()
        d={'*': king_amazon_adj(), '
        for i in board:
            for j in i:
                if j not in 'KA$':
                    d[j] += 1
        return list(d.values())

    return _count()
