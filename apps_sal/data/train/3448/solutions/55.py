def f(n):
    if isinstance(n, str):
        return None
    if n <= 0:
        return None
    if n != int(n):
        return None
    return n * (n + 1) // 2
