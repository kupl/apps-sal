def max_multiple(divisor, bound):
    n = bound
    while (n > 0):
        if n % divisor == 0:
            return n
        n -= 1
    return None
