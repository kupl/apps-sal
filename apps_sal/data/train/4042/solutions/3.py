def points(n):
    return 1 + 4 * sum(((n * n - r * r) ** 0.5 // 1 for r in range(n)))
