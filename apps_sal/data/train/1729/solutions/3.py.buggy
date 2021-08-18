import re

x = 0
y = 0
direction = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def i_am_here(path):
    nonlocal x, y, direction
    for c in re.findall(r'\d+|[rlRL]', path):
        if c == 'r':
            direction = (direction + 1) % 4
        elif c == 'l':
            direction = (direction - 1) % 4
        elif c == 'R':
            direction = (direction + 2) % 4
        elif c == 'L':
            direction = (direction - 2) % 4
        else:
            dx, dy = directions[direction]
            x += int(c) * dx
            y += int(c) * dy
    return [x, y]
