def combine(*args):
    L = max((len(i) for i in args))
    t = []
    j = 0
    while j < L:
        for i in args:
            try:
                t.append(i[j])
            except:
                pass
        j += 1
    return t
