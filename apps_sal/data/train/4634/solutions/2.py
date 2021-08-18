def pac_man(n, pm, enemies):
    row = lambda c="O": [c] * n
    grid = [row() for _ in range(n)]
    grid[pm[0]][pm[1]] = "P"
    for er, ec in enemies:
        grid[er] = row("
        grid=[["
    for er, ec in enemies:
        grid[er][ec]="E"

    edges=[pm]
    count=0
    while edges:
        new_edges=[]
        for er, ec in edges:
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c=er + dr, ec + dc
                if 0 <= r < n and 0 <= c < n:
                    if grid[r][c] == "O":
                        count += 1
                        grid[r][c]="."
                        new_edges.append((r, c))
        edges=new_edges
    return count
