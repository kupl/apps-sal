def grid_index(grid, idxs):
    return ''.join(grid[x][y] for x,y in map(lambda n: divmod(n-1,len(grid)),idxs))
