def T9(words, seq):
    d = {}
    sym = list(map(chr, range(97,123)))
    for x in range(2, 10):
        q = sym[:(3, 4)[x in(7, 9)]]
        sym = sym[(3, 4)[x in(7, 9)]:]
        d[str(x)] = q
    s = zip(words,map(iter, [x.lower()for x in words]))
    return [w for w, i in s if all(next(i)in d[x] for x in seq)] \
           or [''.join(d[x][0] for x in seq)]
