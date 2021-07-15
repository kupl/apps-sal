def multiply(n):
    power = len(str(n)) if n >= 0 else len(str(n)) -1
    return n * 5 ** power
