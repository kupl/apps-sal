def unite_unique(*lists):
    l = [item for lst in lists for item in lst]
    s = set(l)
    return sorted(s, key=l.index)
