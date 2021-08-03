def indices(n, d):
    return [[r] + point for r in range(d + 1)
            for point in indices(n - 1, d - r)] if n > 1 else [[d]]
