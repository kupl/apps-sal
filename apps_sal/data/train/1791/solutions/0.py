from collections import deque
from numpy import cross, dot
MOVES = ((1, 0), (-1, 0), (0, 1), (0, -1))
DIRS = ('v', '^', '>', '<')


def escape(maze):
    start = (x, y) = next(((x, y) for (x, row) in enumerate(maze) for (y, c) in enumerate(row) if c not in '# '))
    (X, Y, dir) = (len(maze), len(maze[0]), MOVES[DIRS.index(maze[x][y])])
    (q, seens) = (deque([(start, dir)]), {})
    if not x or x == X - 1 or (not y) or (y == Y - 1):
        return []
    noPath = True
    while q:
        ((x, y), dir) = q.popleft()
        for (dx, dy) in MOVES:
            (xx, yy) = pos = (x + dx, y + dy)
            if 0 <= xx < X and 0 <= yy < Y and (maze[xx][yy] == ' ') and (pos not in seens):
                q.append((pos, (dx, dy)))
                seens[pos] = ((x, y), dir, (dx, dy))
                if not xx or xx == X - 1 or (not yy) or (yy == Y - 1):
                    (q, noPath) = ([], False)
                    break
    if noPath:
        return []
    path = []
    while pos != start:
        (pos, dir, nextDir) = seens[pos]
        scal = dot(dir, nextDir)
        prod = cross(dir, nextDir)
        if scal:
            path.append('FB' if scal < 0 else 'F')
        else:
            path.append('FL' if prod > 0 else 'FR')
    return list(''.join(path)[::-1])
