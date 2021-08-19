def multiply(n):
    s = str(n)
    factor = len(s)
    if n > 0:
        return n * 5 ** factor
    else:
        return n * 5 ** (factor - 1)
