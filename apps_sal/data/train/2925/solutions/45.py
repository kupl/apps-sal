def multiply(n):
    l = len(str(n)) if n >= 0 else len(str(n)) - 1
    return n * (5 ** l)
