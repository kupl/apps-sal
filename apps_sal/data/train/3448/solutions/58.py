def f(n):
    total = 0
    if isinstance(n, int) and n > 0:
        for b in range(0, n + 1, 1):
            total = total + b
        return total
    else:
        return None
