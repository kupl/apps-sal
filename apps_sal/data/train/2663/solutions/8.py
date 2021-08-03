def addsup(a1, a2, a3):
    l = [[c - b, b, c] for b in a2 for c in a3]
    return list(filter((lambda e: e[0] in a1), l))
