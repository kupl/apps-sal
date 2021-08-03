def generate_pairs(n):
    return [[i, y] for i in range(n + 1) for y in range(i, n + 1)]
