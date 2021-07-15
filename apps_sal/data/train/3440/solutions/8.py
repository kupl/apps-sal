def powers(n):
    return [2**i for i,d in enumerate(bin(n)[::-1]) if d == '1']
