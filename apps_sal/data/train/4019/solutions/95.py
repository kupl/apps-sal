def max_multiple(divisor, bound):
    i = bound
    while True:
        if i % divisor == 0:
            return i
        i-=1

