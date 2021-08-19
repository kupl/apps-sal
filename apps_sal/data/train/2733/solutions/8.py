def last(x):
    from collections import defaultdict
    d = defaultdict(list)
    res = []
    for w in x.split():
        d[w[-1]] += [w]
    for i in range(97, 123):
        res += d[chr(i)]
    return res
