def controller(s):
    (h, v, r, m) = (0, 0, '', 1)
    for i in s:
        if i == 'P':
            v = m if v == 0 else -1 if h == 5 else 1 if h == 0 else 0
        if i == 'O':
            v = -1 if v > 0 else 1 if v < 0 else 0
        if v < 0:
            m = -1
        if v > 0:
            m = 1
        h += v
        h = 0 if h < 0 else 5 if h > 5 else h
        r += str(h)
    return r
