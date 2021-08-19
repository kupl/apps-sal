def max_multiple(divisor, bound):
    for i in range(bound, divisor, -1):
        if i % divisor == 0 and i > 0:
            return i
