def multiply(n):
    m = len(str(n)) if n > 0 else len(str(n)) - 1
    return n * 5 ** m
