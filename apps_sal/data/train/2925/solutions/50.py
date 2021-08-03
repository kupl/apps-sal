def multiply(n):
    l = len(str(n))
    return n * (5**l) if n > 0 else n * (5 ** (l - 1))
