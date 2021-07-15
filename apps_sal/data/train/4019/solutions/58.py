def max_multiple(divisor, bound):
    s = [ x for x in range(1,bound + 1) if x % divisor == 0 and x <= bound]
    return max(s)
