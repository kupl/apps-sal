def ant(g, c, r, n, d=0):
    grid = {(i, j): g[i][j] for j in range(len(g[0])) for i in range(len(g))}
    D = {1: (0, 1), 2: (1, 0), 3: (0, -1), 0: (-1, 0)}
    for i in range(n):
        d = (d + (1 if grid[r, c] == 1 else -1)) % 4
        grid[r, c] = 1 - grid[r, c]
        (R, C) = D[d]
        (r, c) = (r + R, c + C)
        grid[r, c] = 0 if (r, c) not in grid else grid[r, c]
    S = grid.keys()
    (m_y, m_x) = [min(S, key=lambda x: x[i])[i] for i in [0, 1]]
    (M_y, M_x) = [max(S, key=lambda x: x[i])[i] for i in [0, 1]]
    return [[grid.get((m_y + j, m_x + i), 0) for i in range(M_x - m_x + 1)] for j in range(M_y - m_y + 1)]
