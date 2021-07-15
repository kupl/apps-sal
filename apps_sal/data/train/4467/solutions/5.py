def remember(str_):
    d = {}
    seen = set()
    for c in str_:
        if c in seen:
            d[c] = 1
        seen.add(c)
    return list(d)
