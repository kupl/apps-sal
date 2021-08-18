def max_multiple(divisor, bound):
    for n in range(divisor, bound):
        if bound % divisor == 0:
            return bound
        elif n % divisor == 0 and n <= bound and ((n + divisor) > bound):
            return n
