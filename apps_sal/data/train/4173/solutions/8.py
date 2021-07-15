def ant(grid, column, row, n, direction = 0):
    for _ in range(n):
        direction = (direction - 1 + 2*grid[row][column]) % 4
        dx, dy = d[direction]
        grid[row][column] = 1 - grid[row][column]
        row += dy
        column += dx
        if column < 0:
            for i, r in enumerate(grid):
                grid[i] = [0] + r
            column += 1
        elif column >= len(grid[0]):
            for r in grid: r.append(0)
        if row < 0:
            grid = [[0] * len(grid[0])] + grid
            row += 1
        elif row >= len(grid):
            grid.append([0] * len(grid[0]))
    return grid

d = (0, -1), (1, 0), (0, 1), (-1, 0)
