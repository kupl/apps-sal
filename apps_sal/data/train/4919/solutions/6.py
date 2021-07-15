def grid_index(grid, indexes):
    new = []
    for g in grid:
        for el in g:
            new.append(el)
    return ''.join([new[i - 1] for i in indexes])
