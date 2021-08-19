def multiply(n):
    if n >= 0:
        a = str(n)
        return n * 5 ** len(a)
    elif n < 0:
        a = str(n)
        return n * 5 ** (len(a) - 1)
