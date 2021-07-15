def duplicates(array):
    l, out = [], []
    for e in array:
        if e in l and e not in out:
            out.append(e)
        l.append(e)
    return out
