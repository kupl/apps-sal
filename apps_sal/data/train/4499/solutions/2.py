def fracte():
    yield 2
    i = 2
    while True:
        yield 1
        yield i
        yield 1
        i += 2


def convergents_of_e(n):
    fe = fracte()
    an = [next(fe) for f in range(n)]
    n, d = 1, an.pop()
    while an:
        d, n = (d * an.pop() + n), d
    return sum(map(int, str(d)))
