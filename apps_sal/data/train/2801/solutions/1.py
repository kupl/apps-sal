def pattern(n, y=1, z=1, *e):
    res = []
    for i in range(1, n + 1):
        line = ' ' * (i - 1) + str(i % 10) + ' ' * (n - i)
        res.append(patt(line) + cott(patt(line), y))
    res1 = patt(res) + cott(patt(res), z)
    return '\n'.join(res1)


def patt(elem):
    return elem + elem[::-1][1:]


def cott(elem, x):
    return elem[1:] * (x - 1)
