from itertools import cycle


def robot_walk(walks):
    dyx = cycle([(1, 0, 'N'), (0, 1, 'E'), (-1, 0, 'S'), (0, -1, 'W')])
    (ymin, ymax) = (-1, float('inf'))
    (xmin, xmax) = (0, float('inf'))
    (cy, cx) = (0, 0)
    for w in walks:
        (dy, dx, d) = next(dyx)
        (cy, cx) = (cy + dy * w, cx + dx * w)
        if d == 'N':
            if cy >= ymax:
                return True
            ymax = cy
        elif d == 'E':
            if cx >= xmax:
                return True
            xmax = cx
        elif d == 'S':
            if cy <= ymin:
                return True
            ymin = cy
        elif d == 'W':
            if cx <= xmin:
                return True
            xmin = cx
    return False
