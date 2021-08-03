def gimme(a):
    for i in a:
        if i != max(a) and i != min(a):
            return a.index(i)
