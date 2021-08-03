def promenade(choices):

    def compute(): return l + r, m + s

    l, m, r, s = 1, 0, 0, 1
    for c in choices:
        if c == 'L':
            l, m = compute()
        else:
            r, s = compute()

    return compute()
