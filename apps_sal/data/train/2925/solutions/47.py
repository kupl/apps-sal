def multiply(n):
    minus = False
    if n < 0:
        minus = True
        n *= -1
    n *= 5 ** len(str(n))
    if minus:
        n *= -1
    return n
