def solve(s, g):
    f = []
    w = ()
    for i in range(0, s + 1):
        f.append(g * i)
    for i in f:
        if i + g == s:
            w = (g, i)
    return w or -1
