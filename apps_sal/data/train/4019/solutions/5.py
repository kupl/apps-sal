def max_multiple(divisor, bound):
    n = bound
    while n >= divisor:
        if n % divisor == 0:
            return n
        else:
            n -= 1
    if n < divisor:
        return 0
