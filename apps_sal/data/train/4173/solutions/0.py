BLACK = 0
WHITE = 1
CARDINALS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def ant(grid, column, row, n, direction=0):
    r, c, d = row, column, direction
    for _ in range(n):
        if grid[r][c] == BLACK:
            grid[r][c] = WHITE
            d = (d + 3) % 4
        else:
            grid[r][c] = BLACK
            d = (d + 1) % 4
        r, c = r + CARDINALS[d][0], c + CARDINALS[d][1]
        if r < 0:
            grid.insert(0, [0] * len(grid[0]))
            r += 1
        elif r == len(grid):
            grid.append([0] * len(grid[0]))
        elif c < 0:
            grid = [[0] + row for row in grid]
            c += 1
        elif c == len(grid[0]):
            grid = [row + [0] for row in grid]
    return grid
