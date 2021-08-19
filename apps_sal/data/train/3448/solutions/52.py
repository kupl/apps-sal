def f(n):
    n = n
    total = 0
    if type(n) != int:
        return None
    if n <= 0:
        return None
    while n >= 0:
        total += n
        n -= 1
    return total
