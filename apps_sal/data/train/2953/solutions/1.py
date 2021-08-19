from collections import defaultdict


def numericals(s):
    (d, lst) = (defaultdict(int), [])
    for c in s:
        d[c] += 1
        lst.append(d[c])
    return ''.join(map(str, lst))
