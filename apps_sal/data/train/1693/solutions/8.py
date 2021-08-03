from statistics import mean
from math import factorial, log

_lf = []


def logfact(n):
    nonlocal _lf
    CALCLEN = 2200
    if not _lf:
        _lf = [0] * CALCLEN
        for i in range(2, CALCLEN):
            _lf[i] = _lf[i - 1] + log(i)
    return _lf[n]


def unif_ml(xs):
    p1 = mean(xs)
    p2 = max(xs) / 2
    pmle = max(p1, p2)  # probably actually not mle and biased towards 0
    loglh = len(xs) * log(2 * pmle + 1)
    return loglh


def poiss_ml(xs):
    pml = mean(xs)
    loglh = len(xs) * pml + sum([-x * log(pml) + logfact(x) for x in xs])
    return loglh


def solve(xs):
    ul = unif_ml(xs)
    pl = poiss_ml(xs)
    #print('dbg:', ul, pl)
    if ul < pl:
        print('uniform')
    else:
        print('poisson')


def __starting_point():
    v = int(input())
    for i in range(v):
        xs = [int(x) for x in input().split()]
        solve(xs)


__starting_point()
