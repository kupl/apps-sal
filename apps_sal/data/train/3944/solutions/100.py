def sum_triangular_numbers(n):
    # find triangle number
    return sum([i * (i + 1) / 2 for i in range(1, n + 1)])
