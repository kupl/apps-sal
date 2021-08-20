def score_throws(radii):
    return 5 * sum(((r <= 10) + (r < 5) for r in radii)) + (100 if len(radii) and all((r < 5 for r in radii)) else 0)
