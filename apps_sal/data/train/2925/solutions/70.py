def multiply(n):
    return n * 5 ** len(str(abs(n))) if n > 0 else n * 5 ** len(str(abs(n)))
