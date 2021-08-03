def grid_index(grid, indexes):
    unpac_lst = [value for array in grid for value in array]
    return ''.join(unpac_lst[i - 1] for i in indexes)
