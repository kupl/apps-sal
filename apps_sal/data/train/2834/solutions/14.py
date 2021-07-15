def symmetric_point(p, q):
    result = [p[0],q[0]]
    if(p[0] > q[0]):
        result[0] = fromRightToLeft(p[0],q[0])
    else:
        result[0] = fromLeftToRight(p[0],q[0])
    if(p[1] > q[1]):
        result[1] = fromUpToDown(p[1],q[1])
    else:
        result[1] = fromDownToUp(p[1],q[1])
    return result
def fromRightToLeft(p,q):
    return q-abs(p-q)
def fromLeftToRight(p,q):
    return q+abs(p-q)
def fromUpToDown(p,q):
    return q-abs(p-q)
def fromDownToUp(p,q):
    return q+abs(p-q)
