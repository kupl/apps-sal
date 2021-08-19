# precalculate results
LIMIT = 11000        # > 9977 + 104
CACHE = [0]
GRID = set()        # empty grid
x, y = 0, 0        # ant's position
dx, dy = 1, 0        # direction

for _ in range(LIMIT + 1):
    if (x, y) in GRID:      # square is black
        GRID.remove((x, y))
        dx, dy = -dy, dx
    else:                   # square is white
        GRID.add((x, y))
        dx, dy = dy, -dx

    # move forward
    x += dx
    y += dy

    # store number of black squares
    CACHE.append(len(GRID))


def langtons_ant(n):
    if n < LIMIT:
        return CACHE[n]

    # a(n+104) = a(n) + 12 for n > 9976
    x = (n - LIMIT) // 104 + 1
    return CACHE[n - x * 104] + x * 12
