def radix_tree(*a):
    r = {}
    for s in a:
        d = r
        for x in s + '*':
            if x not in d:
                d[x] = {}
            d = d[x]

    def g(d):
        dd = {}
        for x in d:
            d[x] = g(d[x])
            if len(d[x]) == 1:
                (k, v) = [*d[x].items()][0]
                dd[x + k] = v
            else:
                dd[x] = d[x]
        return dd

    def h(d):
        dd = {}
        for x in d:
            d[x] = h(d[x])
            if x != '*':
                dd[x if x[-1] != '*' else x[:-1]] = d[x]
        return dd
    return h(g(r))
