def sum_mul(n, m):
    print(f'n: {n}, m: {m}')
    return sum(range(n, m, n * (1, -1)[m < 0])) if n > 0 and m > 0 else 'INVALID'
