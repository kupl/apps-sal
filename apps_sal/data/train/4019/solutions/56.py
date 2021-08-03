def max_multiple(divisor, bound):
    a = []
    for x in range(divisor, bound + 1):
        if x % divisor == 0:
            a.append(x)
    return max(a)
