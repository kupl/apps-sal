def max_multiple(divisor, bound):
    i = bound
    while i > 1:
        if i % divisor == 0 and i <= bound:
            return i
        i -= 1
