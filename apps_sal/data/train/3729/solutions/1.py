def count_zeros_n_double_fact(n):
    return 0 if n % 2 == 1 else (n // 6250) + (n // 1250) + (n // 250) + (n // 50) + (n // 10)
