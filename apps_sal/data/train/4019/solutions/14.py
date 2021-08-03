def max_multiple(divisor, bound):
    return [x for x in range(divisor * 2, bound + 1, divisor)][-1]
