def balanced_parens(n):
    res = ['']
    for _ in range(n):
        res2 = set()
        for v in res:
            for p in range(len(v) if v else 1):
                res2.add(v[:p] + '()' + v[p:])
        res = list(res2)
    return res
