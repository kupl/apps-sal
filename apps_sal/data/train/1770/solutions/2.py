from math import hypot
from heapq import *

MOVES = ((0, 1), (0, -1), (1, 0), (-1, 0))


def path_finder(maze):
    maze = list(map(list, maze.split()))
    X, Y = end = len(maze) - 1, len(maze[0]) - 1
    q = [(0, 0, 0, (0, 0))]                    # (heuristic, isEnd, n steps, x, y)

    while q and not q[0][1]:
        _, _, c, (x, y) = heappop(q)
        c += 1
        for dx, dy in MOVES:
            pos = a, b = x + dx, y + dy
            if 0 <= a <= X and 0 <= b <= Y and maze[a][b] != 'W':
                maze[a][b] = 'W'
                heappush(q, (c + X - a + Y - b, pos == end, c, pos))

    return q and q[0][1] and q[0][2] or 0
