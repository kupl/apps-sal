def max_multiple(divisor, bound):
    i = 1
    while True:
        if divisor * i > bound:
            return divisor * (i-1)
        else:
            i = i + 1
