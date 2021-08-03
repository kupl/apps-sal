def reverse(a):
    s = list(''.join(a))
    return [''.join(s.pop() for _ in w) for w in a]
