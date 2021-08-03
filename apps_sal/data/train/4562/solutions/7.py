def snap(f, t, n=0, l=None):
    if l is None:
        l = []
    if t == []:
        return n

    l += [f[0]]
    if len(l) > 1 and l[-2] == l[-1]:
        return snap(f[1:] + l, t, n + 1, None)

    l += [t[0]]
    if l[-2] == l[-1]:
        return snap(f[1:] + l, t[1:], n + 1, None)

    return snap(f[1:], t[1:], n, l)
