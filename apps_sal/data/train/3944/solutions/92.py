def sum_triangular_numbers(n):
    return sum((sum(range(i)) for i in range(n + 2)))
