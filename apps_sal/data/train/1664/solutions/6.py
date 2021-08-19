from math import isclose

adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # adjacents moves
knight = [(1, -2), (1, 2), (2, -1), (2, 1), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]   # knight moves
def distance(x1, y1, x2, y2): return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5           # distance between points


def is_diagonal(a, b, i, j): return abs(a - i) == abs(b - j)                            # is point A diagonally aligned with point B?
def is_ok(a, b): return 0 <= a < 8 and 0 <= b < 8                                              # check for corners


def amazon_check_mate(king, amazon):

    board = [['-' for _ in range(8)] for _ in range(8)]

    king = (8 - int(king[1]), 'abcdefgh'.index(king[0]))
    amazon = (8 - int(amazon[1]), 'abcdefgh'.index(amazon[0]))

    board[king[0]][king[1]] = 'K'
    board[amazon[0]][amazon[1]] = 'A'

    def get_adjacents(i, j, s=0): return [[board[i + k][j + l], (i + k, j + l)][s] for k, l in adjacents if is_ok(i + k, j + l)]        # all adjacents of point A

    def assign_check():                                                                                            # assign checks to king from amazon
        for i in range(8):
            for j in range(8):
                if board[i][j] == '-' and (i == amazon[0] or j == amazon[1] or is_diagonal(*amazon, i, j)) and \
                        not isclose(distance(*amazon, *king) + distance(*king, i, j), distance(*amazon, i, j), abs_tol=10e-5):
                    board[i][j] = '#'      # is diagonally aligned and there is not king in between amazon and point A
        for i, j in knight:
            ni, nj = amazon[0] + i, amazon[1] + j
            if is_ok(ni, nj) and board[ni][nj] != 'K':
                board[ni][nj] = '#'

    def assign_king_check():                                                      # our king checks
        for i, j in adjacents:
            ni, nj = king[0] + i, king[1] + j
            if is_ok(ni, nj) and board[ni][nj] != 'A':
                board[ni][nj] = '$'

    def assign_checkmates():                                                      # assign checkmates from amazon
        exceptions = set(get_adjacents(*amazon, 1))
        for i in range(8):
            for j in range(8):
                if board[i][j] == '#' and (i, j) not in exceptions and all(n != '-' for n in get_adjacents(i, j)):
                    board[i][j] = '*'

    def king_amazon_adj():                                                       # special case where amazon and opp. king is adjacent
        adj = get_adjacents(*amazon)
        return adj.count('#') if 'K' in adj else 0

    def assign_safe_not_safe():                                                  # for condition 4
        for i in range(8):
            for j in range(8):
                if board[i][j] == '-' and all(n != '-' for n in get_adjacents(i, j)):
                    board[i][j] = '@'

    def _count():                                                                 # count all the requiremets and characters used
        assign_check()                                                              # '*' => checkmate
        assign_king_check()                                                         # '#' => check
        assign_checkmates()                                                         # '@' => king is on a safe square but it cannot make a valid move
        assign_safe_not_safe()                                                      # '-' => on safe and can make safe move
        d = {'*': king_amazon_adj(), '#': -king_amazon_adj(), '@': 0, '-': 0}
        for i in board:
            for j in i:
                if j not in 'KA$':
                    d[j] += 1
        return list(d.values())

    return _count()                                                               # return final count
