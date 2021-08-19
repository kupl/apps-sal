from itertools import count, takewhile
MOVES = ((0, 1), (1, 1), (1, 0), (-1, 1))


def whoIsWinner(moves, nCon, sz):

    def insideAndSameYet(z):
        (x, y) = z
        return 0 <= x < sz and 0 <= y < sz and (grid[x][y] == who)

    def isWinner(x, y, who):
        for (dx, dy) in MOVES:
            s = 1 + sum((1 for c in (-1, 1) for _ in takewhile(insideAndSameYet, ((x + c * n * dx, y + c * n * dy) for n in count(1)))))
            if s >= nCon:
                return True
        return False
    grid = [[''] * sz for _ in range(sz)]
    xInCols = [0] * sz
    for m in moves:
        who = m[-1]
        y = ord(m[0]) - (65 if m[0].isupper() else 71)
        x = xInCols[y]
        xInCols[y] += 1
        grid[x][y] = who
        if isWinner(x, y, who):
            return who
    else:
        return 'Draw'
