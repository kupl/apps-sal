def reverse(a):
    r = list(''.join(a))
    return [''.join((r.pop() for c in w)) for w in a]
