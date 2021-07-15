def count_zeros_n_double_fact(n): 
    if n % 2 == 1:
        return 0
    return n // 10 + n // 50 + n // 250
