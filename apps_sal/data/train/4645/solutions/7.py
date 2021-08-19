def promenade(ch):

    def evaulate():
        return (l + r, m + s)
    (l, m, r, s) = (1, 0, 0, 1)
    for c in ch:
        if c == 'L':
            (l, m) = evaulate()
        else:
            (r, s) = evaulate()
    return evaulate()
