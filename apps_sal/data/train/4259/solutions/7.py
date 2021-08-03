m, r = lambda s: s + s[-2::-1], lambda s, n: s + s[1:] * n


def pattern(*a):
    n, h = (a + (1,))[:2]
    return '\n'.join(m(list(r(m(' ' * (i - 1) + str(i % 10) + ' ' * (n - i)), h - 1)for i in range(1, n + 1))))
