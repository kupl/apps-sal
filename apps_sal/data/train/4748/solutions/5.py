def insert_dash2(num):
    snum = str(num)
    (evens, odds) = (frozenset('2468'), frozenset('13579'))
    res = []
    for (l, r) in zip(snum[:-1], snum[1:]):
        res.append(l)
        if l in evens and r in evens:
            res.append('*')
        elif l in odds and r in odds:
            res.append('-')
    res.append(snum[-1])
    return ''.join(res)
