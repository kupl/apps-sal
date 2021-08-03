def multiply(n):
    return n * 5**(len(str(n))) if "-" not in str(n) else n * 5**(len(str(n)) - 1)
