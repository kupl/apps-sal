def get_diagonale_code(grid):
    grid = [line.split() for line in grid.split("\n")]
    i, j, d, word = 0, 0, 1, ""
    while 0 <= i < len(grid) and j < len(grid[i]):
        if 0 <= j < len(grid[i]):
            word += grid[i][j]
            i, j = i + d, j + 1
        else: i += d
        if i == 0 or i == len(grid) - 1: d = -d
    return word
