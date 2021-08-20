def similarity(a, b):
    (sa, sb) = (set(a), set(b))
    return len(sa & sb) / len(sa | sb)
