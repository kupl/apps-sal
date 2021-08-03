def multiply(n):
    m = 5**(len(str(n))) if n >= 0 else 5**(len(str(-n)))
    return n * m
