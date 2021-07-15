def max_multiple(divisor, bound):
    l = []
    for int in range(bound + 1):
        if int % divisor == 0:
            l.append(int)
    return max(l)
