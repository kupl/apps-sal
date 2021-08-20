def remove(text, what):
    (t, d) = (list(text), dict(what))
    for (i, c) in enumerate(text):
        n = d.get(c, 0)
        if n:
            d[c] -= 1
            t[i] = ''
    return ''.join(t)
