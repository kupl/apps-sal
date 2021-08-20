def powers(n):
    return [2 ** i for (i, k) in enumerate(bin(n)[::-1]) if k == '1']
