def advice(agents, n):
    # Remove agents outside of bounds
    agents = [(r, c) for r, c in agents if 0 <= r < n and 0 <= c < n]

    # Check for degenerate cases, no agents, or all positions filled
    if n == 0 or len(set(agents)) == n * n:
        return []

    # Place the agents in the field
    field = [[0 for _ in range(n)] for _ in range(n)]
    edges = []
    for r, c in agents:
        field[r][c] = 1
        edges.append((r, c))

    # Flood fill the field in cardinal directions from each edge location that is unfilled
    # Initial edge locations are the positions of the agents
    # Default is all locations if we have no agents
    previous_edges = [(r, c) for r in range(n) for c in range(n)]
    while edges:
        new_edges = []
        for r, c in edges:
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                rr, cc = r + dr, c + dc
                if 0 <= rr < n and 0 <= cc < n and field[rr][cc] == 0:
                    field[rr][cc] = 1
                    new_edges.append((rr, cc))
        previous_edges, edges = edges, new_edges

    # Return the last round of unfilled positions
    return previous_edges
