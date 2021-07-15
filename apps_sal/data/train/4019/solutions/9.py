def max_multiple(divisor, bound):
    last, n = 0, 0
    while n <= bound:
        last = [n, last][n%divisor]
        n += divisor
    return last
