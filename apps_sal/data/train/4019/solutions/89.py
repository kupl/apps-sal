def max_multiple(divisor, bound):
    number = divisor
    while divisor <= bound:
        divisor += number
    return divisor - number
