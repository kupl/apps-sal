def powers(n):
    return [2 ** i for (i, d) in enumerate(f'{n:b}'[::-1]) if d == '1']
