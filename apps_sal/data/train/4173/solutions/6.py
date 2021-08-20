def ant(grid, column, row, n, direction=0):

    def checc(m, k, grid):
        if m > len(grid) - 1:
            grid1 = [[0 for j in range(len(grid[0]))] for i in range(len(grid) + 1)]
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    grid1[i][j] = grid[i][j]
            grid = grid1
        elif m < 0:
            grid1 = [[0 for j in range(len(grid[0]))] for i in range(len(grid) + 1)]
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    grid1[i + 1][j] = grid[i][j]
            m += 1
            grid = grid1
        elif k < 0:
            grid1 = [[0 for j in range(len(grid[0]) + 1)] for i in range(len(grid))]
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    grid1[i][j + 1] = grid[i][j]
            k += 1
            grid = grid1
        elif k > len(grid[0]) - 1:
            grid1 = [[0 for j in range(len(grid[0]) + 1)] for i in range(len(grid))]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    grid1[i][j] = grid[i][j]
            grid = grid1
        return [m, k, grid]
    (m, k) = (row, column)
    dire = direction
    directions = {(1, 0): [0, 1], (1, 1): [0, 2], (1, 2): [0, 3], (1, 3): [0, 0], (0, 0): [1, 3], (0, 1): [1, 0], (0, 2): [1, 1], (0, 3): [1, 2]}
    grids = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
    for l in range(n):
        (m, k, grid) = checc(m, k, grid)
        col = grid[m][k]
        (grid[m][k], dire) = directions[col, dire]
        m += grids[dire][0]
        k += grids[dire][1]
        (m, k, grid) = checc(m, k, grid)
    return grid
