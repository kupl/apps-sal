def max_multiple(divisor, bound):
    temp = max([i for i in range(divisor, bound + 1) if i % divisor == 0 and i <= bound and i > 0])
    return temp
