def powers(n):
    s = bin(n)[::-1]
    return [2**i for i, x in enumerate(s) if x == '1']
