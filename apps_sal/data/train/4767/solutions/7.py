def longest_comb(arr, sign):
    def comb(p): return [[(p, arr[p]), (p + j + 1, i)] for j, i in enumerate(arr[p + 1:]) if [arr[p] > i, arr[p] < i]['<' in sign]]
    m = []
    for i, j in enumerate(arr):
        r = comb(i)
        for k, l in enumerate(r):
            inner = comb(l[-1][0])
            if inner:
                r[k].append(inner.pop()[-1])
            if inner:
                for n in inner:
                    r.append(r[k][:-1] + [tuple(n[-1])])
        m.extend(r)
    l = len(max(m, key=len))
    r = list(map(lambda x: list(map(lambda x: x[1], x)), sorted([i for i in m if len(i) == l], key=lambda x: [i[0] for i in x])))
    return (r if len(r) > 1 else r[0]) if l > 2 else []
