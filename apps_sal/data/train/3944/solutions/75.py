def sum_triangular_numbers(n):
    return sum(((1 + i) * i / 2 for i in range(1, n + 1)))
