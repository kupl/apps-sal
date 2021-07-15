def reverse(a):
    s = iter(''.join(a)[::-1])
    return [''.join(next(s) for _ in range(len(w))) for w in a]
