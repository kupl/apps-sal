def grid_index(grid, indexes):
    flat = sum(grid, [])
    return "".join( flat[i-1] for i in indexes )
