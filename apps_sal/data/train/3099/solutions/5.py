from itertools import count

MOVES = ((0, 1), (1, 1), (1, 0), (-1, 1))


def whoIsWinner(moves, nCon, sz):

    def isWinner(rX, rY, who):
        for dx, dy in MOVES:
            s = 1
            for c in (-1, 1):
                for n in count(1):
                    x, y = rX + c * n * dx, rY + c * n * dy
                    if not (0 <= x < sz and 0 <= y < sz and grid[x][y] == who):
                        break
                    s += 1
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
        return "Draw"
