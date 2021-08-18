import re
moves = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
rotate = {'r': 1, 'l': -1, 'R': 2, 'L': 2}
x, y, d = 0, 0, 0


def i_am_here(path):
    nonlocal x, y, d
    for m in re.findall(r'(r|R|l|L|\d+)', path):
        if m.isalpha():
            d = (d + rotate[m]) % 4
        else:
            dx, dy = moves[d]
            x, y = x + dx * int(m), y + dy * int(m)
    return [x, y]
