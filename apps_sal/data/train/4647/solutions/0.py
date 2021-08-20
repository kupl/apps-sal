def get_neighbourhood(typ, arr, coordinates):

    def isInside(x, y):
        return 0 <= x < len(arr) and 0 <= y < len(arr[0])
    (x, y) = coordinates
    if not isInside(x, y):
        return []
    neigh = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0)] if typ == 'moore' else [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return [arr[a][b] for (a, b) in ((x + dx, y + dy) for (dx, dy) in neigh) if isInside(a, b)]
