from collections import deque
from numpy import cross, dot


MOVES = ((1, 0), (-1, 0), (0, 1), (0, -1))
DIRS = ('v', '^', '>', '<')


def escape(maze):

    start = x, y = next((x, y) for x, row in enumerate(maze) for y, c in enumerate(row) if c not in '# ')
    X, Y, dir = len(maze), len(maze[0]), MOVES[DIRS.index(maze[x][y])]
    q, seens = deque([(start, dir)]), {}

    if not x or x == X - 1 or not y or y == Y - 1:
        return []            # Already at the end, do nothing

    noPath = True
    while q:
        (x, y), dir = q.popleft()
        for dx, dy in MOVES:
            xx, yy = pos = (x + dx, y + dy)

            if 0 <= xx < X and 0 <= yy < Y and maze[xx][yy] == ' ' and pos not in seens:
                q.append((pos, (dx, dy)))
                seens[pos] = ((x, y), dir, (dx, dy))              # data: (origin position, direction before origin, direction after origin)
                if not xx or xx == X - 1 or not yy or yy == Y - 1:      # Escaped!
                    q, noPath = [], False                       # reset the queue to stop it, "from the for loop"
                    break

    if noPath:
        return []                                        # No path, no chocolate...

    path = []
    while pos != start:
        pos, dir, nextDir = seens[pos]
        scal = dot(dir, nextDir)                                # scalar prouct > 0  <=>  go ahead, otherwise, turn back
        prod = cross(dir, nextDir)                              # cross product > 0  <=>  turn left, otherwise, turn right
        if scal:
            path.append('FB' if scal < 0 else 'F')         # dot != 0 => both directions are colinear
        else:
            path.append('FL' if prod > 0 else 'FR')        # orthogonal directions, take a turn

    return list(''.join(path)[::-1])
