def max_multiple(divisor, bound):
    while bound:
        if bound % divisor == 0:
            return bound
        bound -= 1
