def grid_index(grid, indexes):
    flat = tuple(x for e in grid for x in e)
    return ''.join(flat[e - 1] for e in indexes)
