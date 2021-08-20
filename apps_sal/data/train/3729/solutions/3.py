from math import log


def count_zeros_n_double_fact(n):
    return 0 if n & 1 else sum((n // 2 // 5 ** x for x in range(1, int((log(n) - log(2)) / log(5)) + 1)))
