def max_multiple(divisor, bound):
    i=bound
    while i!=0:
        if i%divisor!=0:
            i=i-1
        else:
            return i

