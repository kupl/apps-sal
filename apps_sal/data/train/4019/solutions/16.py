def max_multiple(divisor, bound):
    while bound:
        if not bound % divisor:
            return bound
        bound -= 1
