def sum_triangular_numbers(n):
    return sum([round(a * (a + 1) / 2) for a in range(1, n + 1)])
