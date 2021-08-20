def count_zeros_n_double_fact(n):
    if n % 2 == 1:
        return 0
    res = 0
    working = n // 2
    while working > 0:
        res += working // 5
        working //= 5
    return res
