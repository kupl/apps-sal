from math import hypot

DIRS = {'←': (0, -1), '↑': (-1, 0), '→': (0, 1), '↓': (1, 0),
        '↖': (-1, -1), '↗': (-1, 1), '↘': (1, 1), '↙': (1, -1)}


def count_deaf_rats(town):
    pipper = next((x, y) for x, r in enumerate(town) for y, c in enumerate(r) if c == 'P')
    return sum(isDeaf(pipper, x, y, *DIRS[c])
               for x, r in enumerate(town) for y, c in enumerate(r)
               if c in DIRS)


def isDeaf(pipper, x, y, dx, dy):
    dPipper, dNext = (hypot(*(a - b for a, b in zip(pipper, pos))) for pos in ((x, y), (x + dx, y + dy)))
    return dPipper < dNext
