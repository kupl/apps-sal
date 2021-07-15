def ranks(a):
    b = sorted(a, reverse=True)
    d = {i:b.index(i)+1 for i in a}
    return [d[i] for i in a]
