import operator

def paperwork(n, m):
    if (n<0 or m<0):
        return 0
    return operator.mul(n, m)
