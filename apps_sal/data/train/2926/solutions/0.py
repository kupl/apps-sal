def reverse(a):
    s = reversed(''.join(a))
    return [''.join((next(s) for _ in w)) for w in a]
