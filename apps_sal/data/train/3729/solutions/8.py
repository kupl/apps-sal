def count_zeros_n_double_fact(n):
    fact = 1
    while n > 2:
        fact *= n
        n -= 2
    return len(str(fact)) - len(str(fact).rstrip('0'))
