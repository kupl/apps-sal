def justify(t, w):
    c = t.rfind(' ', 0, w + 1)
    if c == -1 or len(t) <= w:
        return t
    c = t[:c]
    t = t[len(c) + 1:]
    x = ' '
    if c.count(' ') != 0:
        while len(c) != w:
            if w - len(c) >= c.count(x):
                c = c.replace(x, x + ' ')
                x += ' '
            else:
                c = c.replace(x, x + ' ', w - len(c))
    return c + '\n' + justify(t, w)
