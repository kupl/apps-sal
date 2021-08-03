def gimme(a):
    return [a.index(b) for b in a if b != max(a) and b != min(a)][0]
