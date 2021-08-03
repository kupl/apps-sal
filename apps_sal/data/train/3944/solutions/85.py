def t(x): return x * (x + 1) // 2


def sum_triangular_numbers(n):
    return sum(t(x) for x in range(n + 1))
