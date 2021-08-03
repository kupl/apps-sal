def max_multiple(divisor, bound):
    total = 0
    while total <= bound:
        total += divisor
    return total - divisor
