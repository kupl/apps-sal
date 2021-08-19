def multiply(n):
    l = len(str(n))
    if n == 0:
        return 0
    if n > 0:
        return n * 5 ** l
    if n < 0:
        return n * 5 ** (l - 1)
