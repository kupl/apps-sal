from math import hypot
moves = {'↖': (-1, -1), '←': (-1, 0), '↙': (-1, 1), '↑': (0, -1), '↓': (0, 1), '↗': (1, -1), '→': (1, 0), '↘': (1, 1)}


def count_deaf_rats(town_square):
    (deaf, (px, py)) = (0, next(((row.index('P'), y) for (y, row) in enumerate(town_square) if 'P' in row)))

    def dist(x, y):
        return hypot(px - x, py - y)
    for (y, row) in enumerate(town_square):
        for (x, c) in enumerate(row):
            if c in moves:
                (mx, my) = moves[c]
                if dist(x, y) < dist(x + mx, y + my):
                    deaf += 1
    return deaf
