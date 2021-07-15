def max_multiple(divisor, bound):
    return next(i for i in range(bound, 0, -1) if i % divisor == 0)

