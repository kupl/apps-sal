def get_diagonale_code(grid: str) -> str:
    grid = [x.split() for x in grid.splitlines()]
    (res, rows, x) = ('', len(grid), 1)
    r = c = 0
    while -1 < r < rows and c < len(grid[r]):
        res += grid[r][c]
        if r + 1 == rows:
            x = -1
        elif r == 0:
            x = 1
        r += x
        c += 1
    return res
