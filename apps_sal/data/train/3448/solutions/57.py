def f(n):
    if isinstance(n, int) and n > 0:
        sum = 0
        while int(n) > 0:
            sum += n
            n -= 1
        return sum
    return None
