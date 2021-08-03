import math


def shallowest_path(river):
    maxsize = 999999999
    steps = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    h, w = len(river), len(river[0])
    res = [[]] * h
    for r in range(h):
        res[r] = [(maxsize, [(r, 0)])] * w

    points = []
    for r in range(h):
        res[r][0] = (river[r][0], [(r, 0)])
        points.append((r, 0))

    while len(points) > 0:
        p = points.pop(0)
        r, c = p[0], p[1]
        deep = res[r][c][0]
        path = res[r][c][1]
        length = len(path)
        if c < w - 1:
            for s in steps:
                nr = r + s[0]
                nc = c + s[1]
                if nr >= 0 and nr < h and nc >= 0 and nc < w and (nr, nc) not in path:
                    tdeep = res[nr][nc][0]
                    tpath = res[nr][nc][1]
                    tlength = len(tpath)
                    ndeep = max(deep, river[nr][nc])
                    if tdeep > ndeep or (tdeep == ndeep and tlength > length + 1):
                        npath = path.copy()
                        npath.append((nr, nc))
                        res[nr][nc] = (ndeep, npath)
                        if (nr, nc) not in points:
                            points.append((nr, nc))

    min_deep, min_path = maxsize, []
    for r in range(h):
        p = res[r][-1]
        if p[0] < min_deep:
            min_deep, min_path = p[0], p[1]
        elif p[0] == min_deep and len(p[1]) < len(min_path):
            min_deep, min_path = p[0], p[1]
    return min_path
