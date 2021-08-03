def sum_mul(n, m):
    try:
        return sum(i for i in range(n, m, n)) if n > 0 < m else 'INVALID'
    except:
        return 'INVALID'
