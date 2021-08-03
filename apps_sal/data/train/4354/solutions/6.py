def padovan(n, a=1, b=1, c=1):
    return a if n == 0 else padovan(n - 1, b, c, a + b)
