def get_diagonale_code(grid):
    grid = [line.split() for line in grid.splitlines()]
    d, word, N = -1, "", len(grid)
    x, y = 0, 0
    while x < N and y < len(grid[x]):
        if x == 0 or x == N - 1:
            d *= -1
        word += grid[x][y]
        x, y = x + d, y + 1
    return word
