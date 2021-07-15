from operator import sub
def symmetric_point(p, q):
    qp = list(map(sub, p, q))
    return list(map(sub, q, qp))
