def f(n):
    if type(n) is int and n > 0:
        return int(n * (n + 1) / 2)
    else:
        return None
