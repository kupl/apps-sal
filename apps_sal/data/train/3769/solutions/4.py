import re
left = {'right': 'up', 'up': 'left', 'left': 'down', 'down': 'right'}
right = {'right': 'down', 'down': 'left', 'left': 'up', 'up': 'right'}


def execute(s):
    (s, direction) = (re.sub('([RFL])(\\d+)', lambda x: x.group(1) * int(x.group(2)), s), 'right')
    (p, p1, li) = (0, 0, [[0, 0]])
    for i in s:
        if i == 'L':
            direction = left[direction]
        if i == 'R':
            direction = right[direction]
        if i == 'F':
            p1 += (1 if direction == 'right' else -1) if direction in ['left', 'right'] else 0
            p += (1 if direction == 'down' else -1) if direction in ['up', 'down'] else 0
            li.append([p, p1])
    (m, n) = (abs(min(li, key=lambda x: x[0])[0]) + max(li, key=lambda x: x[0])[0], abs(min(li, key=lambda x: x[1])[1]) + max(li, key=lambda x: x[1])[1])
    (p, p1, grid) = (abs(min(li, key=lambda x: x[0])[0]), abs(min(li, key=lambda x: x[1])[1]), [[' ' for _ in range(n + 1)] for _ in range(m + 1)])
    for (i, j) in li:
        grid[p + i][p1 + j] = '*'
    return '\r\n'.join([''.join(i) for i in grid])
