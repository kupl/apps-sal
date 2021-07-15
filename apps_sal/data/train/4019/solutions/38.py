def max_multiple(divisor, bound):
    return int([i for i in range(bound, 0, -1) if i % divisor == 0][0])

