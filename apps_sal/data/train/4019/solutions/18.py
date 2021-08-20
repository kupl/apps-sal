def max_multiple(divisor, bound):
    (a, r) = divmod(bound, divisor)
    return bound - r
