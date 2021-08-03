def sum_mul(n, m):
    if m <= 0 or n < 0:
        return 'INVALID'

    return sum(range(n, m, n)) if n > 0 and m > n else 0 if (n == m and n != 0 and m != 0) or n > m else 'INVALID'
