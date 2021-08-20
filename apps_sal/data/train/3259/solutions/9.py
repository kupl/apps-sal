D = {v: (r, c) for (r, row) in enumerate('abcde123 fghij456 klmno789 pqrst.@0 uvwxyz_/'.split() + ['  ']) for (c, v) in enumerate(row)}


def tv_remote(words):
    (t, lr, lc, lower) = (0, 0, 0, True)
    for e in words:
        if e.isalpha() and lower != e.islower():
            (t, lr, lc) = move(t, lr, lc, 5, 0)
            lower = not lower
        (t, lr, lc) = move(t, lr, lc, *D[e.lower()])
    return t


def move(t, lr, lc, r, c):
    return (t + abs(lr - r) + abs(lc - c) + 1, r, c)
