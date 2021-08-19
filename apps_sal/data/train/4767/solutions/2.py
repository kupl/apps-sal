def longest_comb(a, cmd):
    r = comb(a, {'>>': lambda x, y: x > y, '<<': lambda x, y: x < y}[cmd.replace(' ', '')])
    r = [e for e in r if len(e) == max([len(k) for k in r] + [3])]
    return r[0] if len(r) == 1 else r


def comb(a, op):
    return [[e] for e in a] + [[v] + c for (i, v) in enumerate(a) for c in comb([e for e in a[i:] if op(v, e)], op)]
