def sum_triangular_numbers(n):
    return sum([x * (x + 1) * 0.5 for x in range(1, n + 1)])
