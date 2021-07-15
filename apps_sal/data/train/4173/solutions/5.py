def ant(grid, x, y, n, d=0):
    g, p = {(j, i):v for j, row in enumerate(grid) for i, v in enumerate(row)}, (x, y)
    for m in range(n):
        g[p] = (g[p] + 1) % 2
        d += -1 if g[p] else 1        
        p = p[0] + [0, 1, 0, -1][d % 4], p[1] + [-1, 0, 1, 0][d % 4]
        g[p] = g.get(p, 0) 
        
    return [[g.get((x, y), 0) for x in range(min(x for x, _ in g), max(x for x, _ in g)+1)] for y in range(min(y for _, y in g), max(y for _, y in g)+1)]
