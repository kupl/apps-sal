def max_multiple(divisor, bound):
    output = 0
    while output == 0:
        if bound % divisor == 0:
            output = bound
        bound -= 1

    return bound + 1
