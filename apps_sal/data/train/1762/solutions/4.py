import re


def mouse_path(s):
    x, y, dx, dy, area, vert = 0, 0, 0, 1, 0, [(0, 0)]
    tokes = re.findall('[RL]|\d+', s)
    if len(tokes) % 4 != 3:
        return None
    for n in tokes:
        if n == 'L':
            dx, dy = -dy, dx
        elif n == 'R':
            dx, dy = dy, -dx
        else:
            d = int(n)
            x2, y2 = x + d * dx, y + d * dy
            if any(intersect((x, y), (x2, y2), vert[i], vert[i + 1]) for i in range(len(vert) - 4, -1 + ((x2, y2) == (0, 0)), -2)):
                return None
            area += x * y2 - y * x2
            x, y = x2, y2
            vert.append((x, y))
    if (x, y) != (0, 0):
        return None
    return abs(area) // 2 or None


def intersect(a, b, c, d):
    i = a[0] == b[0]
    return (c[i] - a[i]) * (c[i] - b[i]) <= 0 and (a[1 - i] - c[1 - i]) * (a[1 - i] - d[1 - i]) <= 0
