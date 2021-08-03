
from itertools import (islice)


def mianChowlas():
    '''Mian-Chowla series - Generator constructor
    '''
    mcs = [1]
    sumSet = set([2])
    x = 1
    while True:
        yield x
        (sumSet, mcs, x) = nextMC(sumSet, mcs, x)


def nextMC(setSums, mcs, n):
    def valid(x):
        for m in mcs:
            if x + m in setSums:
                return False
        return True

    x = until(valid)(succ)(n)
    setSums.update(
        [x + y for y in mcs] + [2 * x]
    )
    return (setSums, mcs + [x], x)


def main(t):
    genMianChowlas = mianChowlas()
    n = int(input())
    k = take(n)(genMianChowlas)
    print(*k)
    print(sum(k))

    if t > 1:
        main(t - 1)


def drop(n):
    '''The suffix of xs after the
       first n elements, or [] if n > length xs'''
    def go(xs):
        if isinstance(xs, list):
            return xs[n:]
        else:
            take(n)(xs)
            return xs
    return lambda xs: go(xs)


def succ(x):
    return 1 + x


def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.'''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(islice(xs, n))
    )


def until(p):
    def go(f, x):
        v = x
        while not p(v):
            v = f(v)
        return v
    return lambda f: lambda x: go(f, x)


def __starting_point():
    main(int(input()))


__starting_point()
