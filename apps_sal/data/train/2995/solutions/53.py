def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    elif n <= m:
        return sum(range(n, m, n)) 
    elif n > m:
        return 0
