def close_to_zero(t):
    if len(t) == 0:
        return 0
    x = t.split(' ')
    l = []
    poz = []
    neg = []
    for i in x:
        l.append(int(i))
    for i in l:
        if i == 0:
            return 0
        if i > 0:
            poz.append(i)
        if i < 0:
            neg.append(i)
    if 0 - min(poz) == max(neg):
        return min(poz)
    if 0 - min(poz) > max(neg):
        return min(poz)
    else:
        return max(neg)
