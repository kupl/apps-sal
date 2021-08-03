import re
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)] * 2


def execute(code):
    grid, (dx, dy) = {(0, 0)}, DIRS[0]
    x = y = xm = ym = xM = yM = 0
    for dir, n in re.findall('([FLR])(\d*)', code):
        for _ in range(int(n or '1')):
            if dir == 'L':
                dx, dy = DIRS[DIRS.index((dx, dy)) - 1]
            if dir == 'R':
                dx, dy = DIRS[DIRS.index((dx, dy)) + 1]
            if dir == 'F':
                x += dx
                y += dy
                grid.add((x, y))
                xm, ym, xM, yM = min(xm, x), min(ym, y), max(xM, x), max(yM, y)
    return '\r\n'.join(''.join(' *'[(x, y) in grid] for x in range(xm, xM + 1)) for y in range(ym, yM + 1))
