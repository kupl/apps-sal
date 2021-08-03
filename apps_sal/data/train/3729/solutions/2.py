from functools import reduce


def count_zeros_n_double_fact(n):
    df = n % 2 or reduce(int.__mul__, range(2, n + 1, 2), 1)
    return next(i for i, d in enumerate(f"{df}"[::-1]) if d != "0")
