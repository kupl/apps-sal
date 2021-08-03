def sum_mul(n, m):
    if n and m:
        return sum([x for x in range(n, m, n)]) if n > 0 and m > 0 else 'INVALID'
    return 'INVALID'
