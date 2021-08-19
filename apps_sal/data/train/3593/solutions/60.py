def capitalize(s, ind):
    ind = set(ind)
    return ''.join((l.upper() if i in ind else l for (i, l) in enumerate(s)))
