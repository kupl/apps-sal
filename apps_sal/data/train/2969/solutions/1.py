def advice(agents, n):
    agents = [(a[0], a[1]) for a in agents if 0 <= a[0] < n and 0 <= a[1] < n]
    if len(agents) == n * n or n == 0:
        return []
    grid = [[0] * n for _ in range(n)]
    for ax, ay in agents:
        grid[ax][ay] = 1
    for ax, ay in agents:
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = ax + dx, ay + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                grid[nx][ny] = grid[ax][ay] + 1
                agents.append((nx, ny))
    max_dist = max(d for row in grid for d in row)
    return [(x, y) for x in range(n) for y in range(n) if grid[x][y] == max_dist]
