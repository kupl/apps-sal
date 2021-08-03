def max_multiple(divisor, bound):
    c = []
    for x in range(1, bound + 1):
        if x % divisor == 0 and x <= bound:
            c.append(x)
    return max(c)
