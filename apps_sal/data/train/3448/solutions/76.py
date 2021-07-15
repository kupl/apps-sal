def f(n):
    if type(n) != int:
        return None
    if n <= 0:
        return None
    if n == int(n):
        return 0.5 * n * (n + 1)
    else:
        return None
