import operator

def product(s):
    return operator.mul(*list(map(s.count, '?!')))

