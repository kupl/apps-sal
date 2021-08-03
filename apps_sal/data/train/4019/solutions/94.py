def max_multiple(divisor, bound):
    for num in range(bound, 0, -1):
        if num % divisor == 0:
            return num
    return "none"
