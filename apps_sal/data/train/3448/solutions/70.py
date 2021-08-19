def f(n):
    if type(n) != int or n < 1:
        return None
    else:
        return n * (n + 1) / 2
