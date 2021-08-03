def max_multiple(divisor, bound):
    n = bound
    while n % divisor != 0:
        n -= 1
        if n % divisor == 0:
            break
    return n
