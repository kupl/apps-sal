from itertools import chain


def grid_index(grid, indexes):
    linear = list(chain.from_iterable(grid))
    return ''.join(linear[q - 1] for q in indexes)
