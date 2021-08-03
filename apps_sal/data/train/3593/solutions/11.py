def capitalize(s, ind):
    l = list(s)
    for v in ind:
        if len(l) >= v:
            l[v] = l[v].upper()
    return ''.join(l)
