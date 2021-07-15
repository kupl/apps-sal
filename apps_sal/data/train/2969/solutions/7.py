def advice(agents, n):
    if n <= 0:
        return []
    city = [[-1] * n for _ in range(n)]
    agents = [(i, j) for (i, j) in agents if i >= 0 and j >= 0 and i < n and j < n]
    d = 0
    while agents:
        t = []
        for i, j in agents:
            city[i][j] = d
        d += 1
        for i, j in agents:
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i + di, j + dj
                if x < 0 or y < 0 or x >= n or y >= n or city[x][y] >= 0:
                    continue
                city[x][y] = d
                t.append((x, y))
        agents = t
    m = max(max(r) for r in city)
    return [(i, j) for i in range(n) for j in range(n) if city[i][j] == m] if m != 0 else []
