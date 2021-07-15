def max_multiple(divisor, bound):
    return [i for i in range(divisor,bound+1) if i%divisor==0][-1]
