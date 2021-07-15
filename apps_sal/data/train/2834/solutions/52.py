def symmetric_point(p, q):
    # your code here
    [a,b] = p
    [c,d] = q
    p = c - a
    q = d - b
    return [c+p,d+q]
