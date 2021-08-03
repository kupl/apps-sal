def max_multiple(divisor, bound):
    return max([x for x in range(1, bound + 1) if not x % divisor])
