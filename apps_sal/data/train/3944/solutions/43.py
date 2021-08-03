def sum_triangular_numbers(n):
    return sum(sum(range(i + 1)) for i in range(1, n + 1))
