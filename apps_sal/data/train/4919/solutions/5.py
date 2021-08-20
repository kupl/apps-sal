def grid_index(grid, indexes):
    l = len(grid)
    return ''.join((grid[(i - 1) // l][(i - 1) % l] for i in indexes))
