from itertools import compress
from string import ascii_uppercase, ascii_lowercase
D = {c: i for i, c in enumerate(ascii_uppercase + ascii_lowercase)}


def whoIsWinner(moves, con, sz):
    def gen(i, j):
        for x in range(1, con):
            yield ((i, j - x), (i - x, j), (i + x, j), (i - x, j - x), (i + x, j + x), (i + x, j - x), (i - x, j + x))

    def check(i, j, p):
        memo, count = [True] * 7, [0] * 7
        for L in gen(i, j):
            for x, (k, l) in enumerate(L):
                memo[x] = memo[x] and 0 <= k < sz and 0 <= l < sz and grid[k][l] == p
                count[x] += memo[x]
            if not any(memo):
                return max(count[0], count[1] + count[2], count[3] + count[4], count[5] + count[6]) + 1 >= con
        return True

    if sz >= con <= len(moves):
        grid = [[None] * sz for _ in range(sz)]
        for move in moves:
            i, p = D[move[0]], move[-1]
            j = next(j for j, x in enumerate(grid[i]) if x is None)
            if check(i, j, p):
                return p
            grid[i][j] = p
    return "Draw"
