def sum_mul(n, m):
    print((n, m))
    try:
        return 'INVALID' if n < 1 or m < 1 else sum(range(n, m, n))
    except:
        return 'INVALID'
