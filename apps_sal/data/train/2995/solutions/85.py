def sum_mul(n, m):
    """Some multiples DO"""
    return 'INVALID' if n <= 0 or m <= 0 else sum((n * i for i in range(m) if n * i < m))
