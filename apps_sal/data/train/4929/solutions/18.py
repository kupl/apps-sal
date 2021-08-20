def get_diagonale_code(grid: str) -> str:
    (res, grid) = ('', [x.split() for x in grid.splitlines()])
    (r, c, x, rows) = (0, 0, 1, len(grid))
    while -1 < r < rows and c < len(grid[r]):
        res += grid[r][c]
        if r + 1 == rows:
            x = -1
        elif r == 0:
            x = 1
        r += x
        c += 1
    return res
