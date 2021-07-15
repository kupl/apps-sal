from collections import Counter


def mix(s1, s2):
    res = []
    c1 = Counter([c for c in s1 if c.islower()])
    c2 = Counter([c for c in s2 if c.islower()])
    for c in c1 | c2:       
        if c1[c] > 1 and c1[c] > c2[c]: res += ['1:' + c * c1[c]]
        if c2[c] > 1 and c2[c] > c1[c]: res += ['2:' + c * c2[c]]
        if c1[c] > 1 and c1[c] == c2[c]: res += ['=:' + c * c1[c]]
    return '/'.join(sorted(res, key = lambda a : [-len(a), a]))
