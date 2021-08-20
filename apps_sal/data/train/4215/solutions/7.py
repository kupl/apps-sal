def count_number(n, x):
    return sum((x - n * r <= x % r < 1 for r in range(1, n + 1)))
