def max_multiple(divisor, bound):
    a = bound
    while True:
        if a % divisor == 0:
            return a
        else:
            a -= 1
