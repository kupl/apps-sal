def count_zeros_n_double_fact(n):
    return 0 if n % 2 else sum(n // (10 * 5 ** x) for x in range(len(str(n)) + 1))
