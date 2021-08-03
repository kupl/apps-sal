def knights_tour(p, n):
    (x, y), b, r = p, [[0] * n for _ in range(n)], [None] * n**2
    b[x][y], r[0] = 1, p
    d = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
    def f(x, y): return ((X, Y) for dx, dy in d for X, Y in ((x + dx, y + dy),) if 0 <= X < n and 0 <= Y < n and not b[X][Y])
    for i in range(2, n**2 + 1):
        x, y = min(f(x, y), key=lambda x: sum(1 for _ in f(x[0], x[1])))
        b[x][y], r[i - 1] = i, (x, y)
    return r
