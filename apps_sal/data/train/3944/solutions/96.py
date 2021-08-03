def sum_triangular_numbers(n):
    return sum(x * (x - 1) // 2 for x in range(1, n + 2))
