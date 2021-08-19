from heapq import *
from collections import defaultdict
MOVES = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def shallowest_path(river):
    q = [(river[x][0], 0, (x, 0)) for x in range(len(river))]
    path = {}
    stored_steps = defaultdict(lambda: float('inf'))
    heapify(q)
    while q:
        (cost, step, (x, y)) = heappop(q)
        if (x, y) == (x, len(river[0]) - 1):
            end = (x, y)
            break
        for (dx, dy) in MOVES:
            xx = dx + x
            yy = dy + y
            if 0 <= xx < len(river) and 0 <= yy < len(river[0]):
                new_step = step + 1
                if new_step < stored_steps[xx, yy]:
                    stored_steps[xx, yy] = new_step
                    new_cost = max(cost, river[xx][yy])
                    path[xx, yy] = (x, y)
                    heappush(q, (new_cost, new_step, (xx, yy)))
    coords = [end]
    while coords[-1][1] != 0:
        coords.append(path[end])
        end = path[end]
    return coords[::-1]
