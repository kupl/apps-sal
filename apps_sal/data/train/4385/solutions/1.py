def generate_pairs(n):
    return [[a, b] for a in range(n + 1) for b in range(a, n + 1)]
