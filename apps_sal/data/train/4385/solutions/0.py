def generate_pairs(n):
    return [[i, j] for i in range(n + 1) for j in range(i, n + 1)]
