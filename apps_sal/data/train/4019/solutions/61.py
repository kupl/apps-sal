def max_multiple(divisor, bound):
    for num in range(bound):
        if not (bound - num) % divisor:
            return bound - num
