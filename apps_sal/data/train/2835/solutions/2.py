from itertools import count, islice


def postponed_sieve():
    yield 2
    yield 3
    yield 5
    yield 7
    sieve = {}
    ps = postponed_sieve()
    p = next(ps) and next(ps)
    q = p * p
    for c in count(9, 2):
        if c in sieve:
            s = sieve.pop(c)
        elif c < q:
            yield c
            continue
        else:
            s = count(q + 2 * p, 2 * p)
            p = next(ps)
            q = p * p
        for m in s:
            if m not in sieve:
                break
        sieve[m] = s


def sequence():
    for d in postponed_sieve():
        yield from str(d)


def solve(s, l):
    return ''.join(islice(sequence(), s, s + l))
