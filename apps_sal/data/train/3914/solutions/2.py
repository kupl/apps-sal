def dominator(a):
    return ([x for x in set(a) if a.count(x) > len(a) / 2][:1] or [-1])[0]
