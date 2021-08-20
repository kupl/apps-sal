def count_zeros_n_double_fact(n):
    if n % 2:
        return 0
    (s, n) = (0, n // 2)
    while n >= 5:
        n //= 5
        s += n
    return s
