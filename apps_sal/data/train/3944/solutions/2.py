def sum_triangular_numbers(n):
    return sum((sum(range(x + 1)) for x in range(n + 1)))
