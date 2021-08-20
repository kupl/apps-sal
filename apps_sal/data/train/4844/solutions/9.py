def get_password(grid, directions):
    for each in grid:
        if 'x' in each:
            x = int([grid.index(each)][0])
            y = int([each.index('x')][0])
            break
    res = ''
    for each in directions:
        if each[0:2] == 'ri':
            y += 1
            if each[-1:] == 'T':
                res += grid[x][y]
        elif each[0:2] == 'le':
            y -= 1
            if each[-1:] == 'T':
                res += grid[x][y]
        elif each[0:2] == 'up':
            x -= 1
            if each[-1:] == 'T':
                res += grid[x][y]
        elif each[0:2] == 'do':
            x += 1
            if each[-1:] == 'T':
                res += grid[x][y]
    return res
