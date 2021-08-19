def multiply(n):
    if n >= 0:
        b = 5 ** len(str(n))
        return n * b
    elif n < 0:
        n = abs(n)
        b = 5 ** len(str(n))
        return -abs(n * b)
