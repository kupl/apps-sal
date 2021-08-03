def max_multiple(divisor, bound):
    return max(list(i for i in range(1, bound + 1) if i % divisor == 0))
