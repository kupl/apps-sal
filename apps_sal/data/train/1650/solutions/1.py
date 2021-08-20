def find_all(s, d):
    xs = [x for x in digs(d) if sum(x) == s]
    if not xs:
        return []
    else:

        def reduce_int(xs):
            return int(''.join(map(str, xs)))
        min = reduce_int(xs[0])
        max = reduce_int(xs[-1])
        return [len(xs), min, max]


def digs(d, start=1):
    """
    >>> list(digs(3, start=9))
    [[9, 9, 9]]
    >>> list(digs(2, start=8))
    [[8, 8], [8, 9], [9, 9]]
    """
    if d == 1:
        for x in range(start, 10):
            yield [x]
    else:
        for x in range(start, 10):
            for y in digs(d - 1, x):
                yield ([x] + y)
