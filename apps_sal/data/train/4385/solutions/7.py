def generate_pairs(n):
    return [[i, x] for i in range(n + 1) for x in range(n + 1) if x >= i]
