LIMIT = 11000
CACHE = [0]
GRID = set()
(x, y) = (0, 0)
(dx, dy) = (1, 0)
for _ in range(LIMIT + 1):
    if (x, y) in GRID:
        GRID.remove((x, y))
        (dx, dy) = (-dy, dx)
    else:
        GRID.add((x, y))
        (dx, dy) = (dy, -dx)
    x += dx
    y += dy
    CACHE.append(len(GRID))


def langtons_ant(n):
    if n < LIMIT:
        return CACHE[n]
    x = (n - LIMIT) // 104 + 1
    return CACHE[n - x * 104] + x * 12
