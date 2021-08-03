def multiply(n):
    a = len(str(n))
    if n >= 0:
        return n * 5 ** a
    return n * 5 ** (a - 1)
