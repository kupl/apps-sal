def flatten(*a):
    r, s = [], [iter(a)]
    while s:
        it = s.pop()
        for v in it:
            if isinstance(v, list):
                s.extend((it, iter(v)))
                break
            else:
                r.append(v)
    return r
