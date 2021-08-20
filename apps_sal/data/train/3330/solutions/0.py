def make_triangle(m, n):
    (lns, sm) = (0, 0)
    while sm < n - m + 1:
        lns += 1
        sm += lns
    if sm > n - m + 1:
        return ''
    matrix = [[0] * (i + 1) for i in range(lns)]
    (y, x, s) = (0, 0, 0)
    ds = ((1, 1), (0, -1), (-1, 0))
    (dy, dx) = ds[s]
    for i in range(m, n + 1):
        matrix[y][x] = str(i % 10)
        if not 0 <= y + dy < len(matrix) or not 0 <= x + dx < len(matrix[y + dy]) or matrix[y + dy][x + dx]:
            s += 1
            (dy, dx) = ds[s % 3]
        (y, x) = (y + dy, x + dx)
    return '\n'.join((' '.join(ln).center(len(matrix[-1]) * 2 - 1).rstrip() for ln in matrix))
