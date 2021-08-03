def max_multiple(divisor, bound):
    return max([n for n in range(divisor, bound + 1) if n % divisor == 0])
