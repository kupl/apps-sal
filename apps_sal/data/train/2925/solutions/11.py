def multiply(n):
    return n * 5 ** (len(str(n)) - (1 if n < 0 else 0))
