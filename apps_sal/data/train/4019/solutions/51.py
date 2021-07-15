def max_multiple(divisor, bound):
    lst=[x for x in range(bound+1) if x%divisor==0]
    return lst[-1]
