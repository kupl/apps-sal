def multiply(n):
    if n >= 0:
        a = len(str(n))
        return n * 5 ** a
    elif n < 0:
        a = len(str(n)) - 1
        return n * 5 ** a
