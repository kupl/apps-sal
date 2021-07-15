def max_multiple(divisor, bound):
    while bound > 0 and bound%divisor != 0:
        bound += -1
    return bound
