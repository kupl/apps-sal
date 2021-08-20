d = dict(zip('123456789', [' '] + 'ABC DEF GHI JKL MNO PQRS TUV WXYZ'.split()))


def T9(w, p):
    return [i for i in w if all((k in d[l] for (k, l) in zip(i.upper(), p)))] or [''.join((d[i][0] for i in p)).lower()]
