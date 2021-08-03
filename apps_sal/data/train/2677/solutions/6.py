SHIFT = 'aA'
syms = {
    x: (i, j)
    for i, row in enumerate([
        'abcde123',
        'fghij456',
        'klmno789',
        'pqrst.@0',
        'uvwxyz_/',
    ])
    for j, x in enumerate(row)
}
syms[' '] = (5, 1)
syms[SHIFT] = (5, 0)


def tv_remote(words):
    r = c = 0
    n = 0
    lower = True

    def press(x):
        nonlocal n, r, c, lower
        r1, c1 = syms[x]
        n += min(abs(r1 - r), 6 - abs(r1 - r)) + min(abs(c1 - c), 8 - abs(c1 - c)) + 1
        r, c = r1, c1
        if x == SHIFT:
            lower = not lower

    for ch in words:
        if ch.isalpha() and ch.islower() != lower:
            press(SHIFT)
        press(ch.lower())
    return n
