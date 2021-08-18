def max_multiple(divisor, bound):
    while bound > divisor:
        if bound % divisor == 0:
            return bound
        else:
            bound = bound - 1
            return max_multiple(divisor, bound)
