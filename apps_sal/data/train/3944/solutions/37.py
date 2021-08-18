def sum_triangular_numbers(n):
    return sum([(i + 1) * i / 2 for i in range(1, n + 1)])
