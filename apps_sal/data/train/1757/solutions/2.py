from heapq import *
MOVES = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]


def knights_tour(start, size):

    seen = set([start])
    path = [start]

    for i in range(size * size):
        q = []
        x, y = start
        for dx, dy in MOVES:
            xx = x + dx
            yy = y + dy
            if (xx, yy) not in seen and (0 <= xx < size and 0 <= yy < size):
                c = 0
                for a, b in MOVES:
                    xxx = xx + a
                    yyy = yy + b
                    if (xxx, yyy) not in seen and (0 <= xxx < size and 0 <= yyy < size):
                        c += 1
                heappush(q, (c, (xx, yy)))

        if q:
            start = heappop(q)[1]
            path.append(start)
            seen.add(start)

    return path
