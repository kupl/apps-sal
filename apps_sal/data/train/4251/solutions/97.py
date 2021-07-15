def difference_of_squares(n):
    return ((1 + n) * n // 2) ** 2 - sum(map(lambda x: x * x, range(1, n + 1)))
