def max_multiple(divisor, bound):
    for x in range(bound + 1):
        if (bound - x) % divisor == 0:
            return bound - x
