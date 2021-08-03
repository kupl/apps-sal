def solution(a, b):
    alen = len(a)
    blen = len(b)
    c = []
    if alen < blen:
        c.append(a)
        c.append(b)
        c.append(a)
    elif blen < alen:
        c.append(b)
        c.append(a)
        c.append(b)
    c = "".join(c)
    return c
