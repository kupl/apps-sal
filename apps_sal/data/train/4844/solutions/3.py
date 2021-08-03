def get_password(grid, directions):
    res = ''
    for i in range(len(grid)):
        if 'x' in grid[i]:
            pos = [i, grid[i].index('x')]
    for i in directions:
        if i[0] == 'l':
            pos[1] -= 1
        elif i[0] == 'd':
            pos[0] += 1
        elif i[0] == 'r':
            pos[1] += 1
        else:
            pos[0] -= 1
        if i[-1] == 'T':
            res += grid[pos[0]][pos[1]]
    return res
