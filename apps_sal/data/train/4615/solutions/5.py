def logistic_map(width, height, xs, ys):
    neighbours = lambda c: {(c[0] + i, c[1] + j)
                    for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]
                        if 0 <= c[0] + i < width and 0 <= c[1] + j < height}
    grid = [[None] * width for _ in range(height)]
    distance, seen, bag = 0, set(), set(zip(xs, ys))
    while bag:
        for x, y in bag:
            grid[y][x] = distance
        seen |= bag
        bag = set.union(*map(neighbours, bag)) - seen
        distance += 1
    return grid
