def sum_triangular_numbers(n):
    return sum([n * (n + 1) // 2 for n in range(1, n + 1)])
