def ant(grid, column, row, n, dir=0):
    w, d = len(grid[0]), len(grid)
    m = [[0 for i in range(w + 2 * n)] for j in range(d + 2 * n)]
    for i in range(d):
        m[i + n][n:n + w] = grid[i][:]
    x, y = column + n, row + n
    t = 0
    xmax, xmin = x, x
    ymax, ymin = y, y
    for _ in range(n):
        dir += (m[y][x] == 1) * (1) + (m[y][x] == 0) * (-1)
        dir %= 4
        m[y][x] = 1 - m[y][x]
        y += (dir == 0) * (-1) + (dir == 2) * 1
        x += (dir == 3) * (-1) + (dir == 1) * 1
        xmax, xmin = max(xmax, x), min(xmin, x)
        ymax, ymin = max(ymax, y), min(ymin, y)
    return [m[i][min(xmin, n):max(xmax, n + w - 1) + 1] for i in range(min(ymin, n), max(ymax, n + d - 1) + 1)]
