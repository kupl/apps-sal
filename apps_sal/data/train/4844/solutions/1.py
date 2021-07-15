def get_password(grid, directions):
    r, c = [(r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == 'x'].pop()
    p = ''
    for d in directions:
        r, c = (r + {'d':1, 'u':-1}.get(d[0], 0), c + {'r':1, 'l':-1}.get(d[0], 0))
        if d[-1] == 'T': p += grid[r][c]
    return p
