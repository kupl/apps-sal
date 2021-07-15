def max_multiple(divisor, bound):
    n = [x for x in range(bound+1) if x%divisor==0]
    return max(n)

