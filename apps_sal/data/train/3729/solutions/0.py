def count_zeros_n_double_fact(n): 
    if n % 2 != 0:
        return 0
    k = 0
    while n >= 10:
        k += n // 10
        n //= 5
    return k
