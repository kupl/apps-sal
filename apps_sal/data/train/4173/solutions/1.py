def ant(grid, c, r, n, direction=0):
    MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dims = {(min, 0): 0, (max, 0): len(grid) - 1, (min, 1): 0, (max, 1): len(grid[0]) - 1}
    gridWhite = {(x, y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y]}
    for _ in range(n):
        direction = (direction + (-1) ** ((r, c) not in gridWhite)) % 4
        gridWhite ^= {(r, c)}
        r += MOVES[direction][0]
        c += MOVES[direction][1]
        for (func, dim) in dims:
            dims[func, dim] = func(dims[func, dim], (r, c)[dim])
    (MinX, MinY) = (dims[min, 0], dims[min, 1])
    (lenX, lenY) = (dims[max, 0] - MinX + 1, dims[max, 1] - MinY + 1)
    return [[1 if (x + MinX, y + MinY) in gridWhite else 0 for y in range(lenY)] for x in range(lenX)]
