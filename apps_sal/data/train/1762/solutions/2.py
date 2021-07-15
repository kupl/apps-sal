import re

def check_intersection(y, x0, x1, segments):
    return any(x0 <= x <= x1 and y0 <= y <= y1 for x, y0, y1 in segments)

def mouse_path(s):
    sort_coords = lambda x0, x1: (x0, x1) if x0 <= x1 else (x1, x0)
    dx, dy = 1, 0
    x, y = 0, 0
    hs, vs = [], []
    area = 0
    s = re.split('([LR])', s)
    n = len(s)
    for i in range(n):
        cmd = s[i]
        if cmd == 'L':
            dx, dy = -dy, dx
        elif cmd == 'R':
            dx, dy = dy, -dx
        else:
            d = int(cmd)
            x1, y1 = x + d * dx, y + d * dy
            if dy == 0:
                a, b = sort_coords(x, x1)
                if i == n - 1:
                    return None
                if check_intersection(y, a, b, vs[:-1]):
                    return None
                hs.append((y, a, b))
            else:
                a, b = sort_coords(y, y1)
                if i == n - 1:
                    hs = hs[1:]
                if check_intersection(x, a, b, hs[:-1]):
                    return None
                vs.append((x, a, b))
            area += x * y1 - x1 * y
            x, y = x1, y1
    return abs(area // 2) if x == 0 and y == 0 else None
