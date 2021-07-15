def multiply(n):
    return n * 5 ** (lambda n: len(str(n)) if n >= 0 else len(str(n))-1)(n)
