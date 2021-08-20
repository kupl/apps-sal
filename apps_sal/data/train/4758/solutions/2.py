from itertools import zip_longest


def connect_four_place(columns):
    grid = [[] for _ in [0] * 7] + ['-' * 6]
    for (i, c) in enumerate(columns):
        grid[c].append('YR'[i % 2])
    return [list(l[:-1]) for l in zip_longest(*grid, fillvalue='-')][::-1]
