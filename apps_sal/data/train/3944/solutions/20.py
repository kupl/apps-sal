def sum_triangular_numbers(n):
    return sum((i * (i + 1) // 2 for i in range(n + 1)))


def sum_triangular_numbers(n):
    return sum((i * (n - i + 1) for i in range(n + 1)))


def sum_triangular_numbers(n):
    return max(0, n * (n + 1) * (n + 2) // 6)


def sum_triangular_numbers(n):
    return 0 if n < 1 else n * (n + 1) * (n + 2) // 6
