def max_multiple(divisor, bound):
    b = []
    for i in range(bound + 1):
        if i % divisor == 0:
            b.append(i)
    return b[-1]
