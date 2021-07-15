def sum_mul(n, m):
    try:
        return sum(i for i in range(n, m, n)) if m > 0 and n > 0 else 'INVALID'
    except:
        return 'INVALID'
