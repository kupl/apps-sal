direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
operations = {'l': +1, 'r': -1, 'L': -2, 'R': 2}
vector = 2
position = [0, 0]


def i_am_here(path):
    nonlocal vector, position
    step = 0
    for c in path:
        if c.isnumeric():
            step = step * 10 + int(c)
        else:
            if step > 0:
                position = [position[0] + direction[vector][0] * step, position[1] + direction[vector][1] * step]
                step = 0
            step = 0
            o = operations.get(c)
            vector += o
            vector %= len(direction)
    if step > 0:
        position = [position[0] + direction[vector][0] * step, position[1] + direction[vector][1] * step]
    return position
