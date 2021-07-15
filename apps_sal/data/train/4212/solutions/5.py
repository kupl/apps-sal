def unite_unique(*args):
    a = []
    for e in args:
        for x in e:
            if x not in a:
                a.append(x)
    return a
