def max_multiple(divisor, bound):
    x = []
    for n in range(divisor, bound + 1):
        if n % divisor == 0 and n <= bound and (n > 0):
            x.append(n)
        else:
            pass
    return max(x)
