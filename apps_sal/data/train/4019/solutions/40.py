def max_multiple(divisor, bound):
    for loop in range(bound, 0, -1):
        if loop % divisor == 0 and loop > 0:
            return loop
