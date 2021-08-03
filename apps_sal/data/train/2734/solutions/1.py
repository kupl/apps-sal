def peaceful_yard(yard, min_distance):
    # Extract cat positions
    cats = {ch: (r, c) for r, row in enumerate(yard) for c, ch in enumerate(row) if ch != "-"}
    if len(cats) < 2:
        return True
    # Extract coordinates amd calculate euclidean distances between them
    coords = list(cats.values())
    def euc_dist(x, y): return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
    r = list(range(len(coords)))
    dists = [euc_dist(coords[i], coords[j]) for i in r for j in r if i < j]
    # Check minimum distance against required minimum
    return min_distance <= min(dists)
