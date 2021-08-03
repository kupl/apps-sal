def getHorizontal(s, x): return s + s[1:] * (x - 1)


def pattern(n, x=1, y=1, *a):
    if n < 1:
        return ''
    l, x, y = 2 * n - 1, max(1, x), max(1, y)
    sngl = [getHorizontal('{}{}{}'.format(z % 10, ' ' * (l - 2 * z), z % 10 if z != n else '').center(l), x) for z in range(1, n + 1)]
    cross = sngl + sngl[:-1][::-1]
    return '\n'.join(cross + cross[1:] * (y - 1))
