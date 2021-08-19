D = {c: i for (c, i) in zip('abcdefghijklmnopqrstuvwxyz', '22233344455566677778889999')}


def T9(words, seq):
    r = [w for w in words if ''.join((D[c] for c in w.lower())) == seq]
    return r if r else [''.join(({i: c for (i, c) in zip('23456789', 'adgjmptw')}[i] for i in seq))]
