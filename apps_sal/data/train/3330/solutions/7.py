def make_triangle(start, end):
    from itertools import cycle
    from math import sqrt

    rows = sqrt(8 * (end - start) + 9) / 2 - .5
    if not rows.is_integer():
        return ''

    rows = int(rows)
    row, col, fill = -1, -1, start
    ls = [[''] * n for n in range(1, rows + 1)]
    directions = cycle([(1, 1), (0, -1), (-1, 0)])

    for i in range(rows):
        dir = next(directions)

        for j in range(rows - i):
            row += dir[0]
            col += dir[1]
            ls[row][col] = str(fill % 10)
            fill += 1

    return '\n'.join(' ' * (rows - i - 1) + ' '.join(r) for i, r in enumerate(ls))
