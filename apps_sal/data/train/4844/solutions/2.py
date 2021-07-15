DIRS = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0),
}

def get_password(grid, directions):
    i, j = next((i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 'x')
    pw = ''
    for d in directions:
        take = d.endswith('T')
        i_delta, j_delta = DIRS[d.rstrip('T')]
        i += i_delta
        j += j_delta
        if take:
            pw += grid[i][j]
    return pw
