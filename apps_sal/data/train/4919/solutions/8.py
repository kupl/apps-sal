def grid_index(grid, indexes):
    n = len(grid)
    idxs = (i - 1 for i in indexes)
    return ''.join((grid[i // n][i % n] for i in idxs))
