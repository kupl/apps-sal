def bubblesort_once(l):
    if len(l) < 2:
        return l[:]

    lst, mx = [], l[0]
    for v in l[1:]:
        if mx < v:
            mx, v = v, mx
        lst.append(v)
    lst.append(mx)
    return lst
