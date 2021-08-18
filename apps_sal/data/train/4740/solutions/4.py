def row_sum_odd_numbers(n):
    a, b = n * (n - 1) + 1, n * (n + 1)
    return sum(range(a, b, 2)) if a != 1 else 1
