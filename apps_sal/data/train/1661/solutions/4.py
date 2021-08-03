import re
from collections import defaultdict, deque


def execute(code):
    dirs = deque([(0, 1), (-1, 0), (0, -1), (1, 0)])
    yarr, xarr = [0], [0]
    while True:
        code, n = re.subn('\(([^()]+)\)(\d*)', lambda m: m.group(1) * int(m.group(2) or 1), code)
        if not n:
            break
    for c in ''.join(a * int(b or 1) for a, b in re.findall('(\D)(\d*)', code)):
        if c == 'F':
            dy, dx = dirs[0]
            xarr.append(xarr[-1] + dx)
            yarr.append(yarr[-1] + dy)
        if c == 'L':
            dirs.rotate(-1)
        if c == 'R':
            dirs.rotate(1)
    xmin, xmax = min(xarr), max(xarr)
    ymin, ymax = min(yarr), max(yarr)
    d = dict(zip(zip(yarr, xarr), '*' * len(xarr)))
    return '\r\n'.join(''.join(d.get((y, x), ' ') for x in range(xmin, xmax + 1)) for y in range(ymin, ymax + 1))
