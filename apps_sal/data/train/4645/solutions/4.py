def promenade(choices):
    l, m, r = [1, 0], [1, 1], [0, 1]
    for c in choices:
        if c == 'L':
            l = m[:]
        else:
            r = m[:]
        m = [l[0] + r[0], l[1] + r[1]]
    return tuple(m)
