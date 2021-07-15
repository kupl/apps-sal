def grid_index(grid, indexes):
    grid = sum(grid, start=[''])
    return ''.join(grid[i] for i in indexes)
