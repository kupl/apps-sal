def solution(a, b):
    c = []
    if len(a) > len(b):
        c.extend(b)
        c.extend(a)
        c.extend(b)
        return (''.join(c))
    if len(b) > len(a):
        c.extend(a)
        c.extend(b)
        c.extend(a)
        return (''.join(c))

    pass
