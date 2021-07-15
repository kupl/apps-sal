def max_multiple(divisor, bound):
    return [x for x in range(bound + 1)[::-1] if x % divisor == 0][0]
