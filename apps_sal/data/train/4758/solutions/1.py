from itertools import cycle, zip_longest
(EMPTY_CELL, HIGH, WIDTH) = ('-', 6, 7)


def connect_four_place(columns):
    (player, cols) = (cycle(['Y', 'R']), [[] for _ in range(WIDTH)])
    for c in columns:
        cols[c].append(next(player))
    while len(cols[0]) < HIGH:
        cols[0].append(EMPTY_CELL)
    return [list(l) for l in zip_longest(*cols, fillvalue=EMPTY_CELL)][::-1]
