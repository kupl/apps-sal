import operator
def symmetric_point(p, q):
    return [i*-1+j*2 for i,j in zip(p,q)]
