from heapq import *
MOVES = tuple(((dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if dx or dy))


def shallowest_path(river):
    (lX, lY) = (len(river), len(river[0]))
    pathDct = {}
    cost = [[(float('inf'), float('inf'))] * lY for _ in range(lX)]
    for x in range(lX):
        cost[x][0] = (river[x][0], 1)
    q = [(river[x][0], lY == 1, 1, (x, 0)) for x in range(lX)]
    heapify(q)
    while not q[0][1]:
        (c, _, steps, pos) = heappop(q)
        (x, y) = pos
        for (dx, dy) in MOVES:
            (a, b) = new = (x + dx, y + dy)
            if 0 <= a < lX and 0 <= b < lY:
                check = (nC, nS) = (max(c, river[a][b]), steps + 1)
                if cost[a][b] > check:
                    cost[a][b] = check
                    pathDct[new] = pos
                    heappush(q, (nC, b == lY - 1, nS, new))
    (path, pos) = ([], q[0][-1])
    while pos:
        path.append(pos)
        pos = pathDct.get(pos)
    return path[::-1]
