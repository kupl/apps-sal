def unite_unique(*arrs):
    seen = set()
    return [i for a in arrs for i in a if not (i in seen or seen.add(i))]
