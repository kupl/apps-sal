def max_multiple(d, b):
    return max([x for x in range(1, b + 1) if x % d == 0])
