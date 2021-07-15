def multiply(n):
    return n * (5 ** len(list(str(n)))) if n > 0 else n * (5 ** len(list(str(n*-1))))
