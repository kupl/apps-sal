def sum_mul(n, m):
    if n > 0 and m > 0:
        return sum(list([x for x in range(n, m) if x % n == 0]))
    else:
        return 'INVALID'
