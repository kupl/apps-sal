def range_parser(inp):
    res = []
    for r in inp.split(','):
        r = list(map(int, r.replace(':', '-').split('-')))
        if len(r) > 1:
            r[1] += 1
            res += range(*r)
        else:
            res.append(r[0])
    return res
