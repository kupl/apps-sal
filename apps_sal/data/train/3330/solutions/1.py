from itertools import cycle
from math import sqrt


def make_triangle(start, end):
    rows = sqrt(8 * (end - start) + 9) / 2 - .5

    if not rows.is_integer():
        return ''

    rows = int(rows)
    row, col, value = -1, -1, start

    directions = cycle([(1, 0), (0, -1), (-1, 1)])
    triangle = [[''] * n for n in range(1, rows + 1)]

    for times in range(rows, 0, -1):
        cur_dir = next(directions)

        for _ in range(times):
            row += cur_dir[0]
            col += cur_dir[1]

            triangle[row][col] = str(value % 10)
            value += 1

    return "\n".join(' ' * (rows - i - 1) + ' '.join(r) for i, r in enumerate(triangle))

