def logistic_map(width,height,xs,ys):
    grid = []
    supply = [(xs[i],ys[i]) for i in range(len(xs))]
    for y in range(height):
        grid.append([])
        for x in range(width):
            grid[y].append(min([abs(x - sx) + abs(y - sy) for sx,sy in supply]) if supply else None)
    return grid
