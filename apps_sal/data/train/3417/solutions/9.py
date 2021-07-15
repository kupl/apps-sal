def cut_the_ropes(a):
    r = []
    while a:
        r.append(len(a))
        n = min(a)
        a = [x - n for x in a if x != n]
    return r
