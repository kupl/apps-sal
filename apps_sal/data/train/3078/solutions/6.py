def array_center(a):
    mi, me = min(a), sum(a)/len(a)
    return [x for x in a if abs(x-me) < mi]
