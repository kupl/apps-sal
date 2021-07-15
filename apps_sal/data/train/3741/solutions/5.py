def vector_affinity(*args):
    l1,l2 = list(map(len,args))
    return sum(x==y for x,y in zip(*args)) / (1.0 * (max(l1,l2))) if l1 or l2 else 1.0
