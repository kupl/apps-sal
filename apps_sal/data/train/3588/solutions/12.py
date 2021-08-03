def quadratic(x1, x2):
    if x1 or x2 >= 0:
        sum = x1 + x2
        mult = x1 * x2
        return 1, -sum, mult
    if x1 or x2 <= 0:
        sum1 = x1 + x2
        mult1 = x1 * x2
        return 1, sum1, mult1
