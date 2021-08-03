import re


def s(m):
    n, w = m.groups()
    n = int(n)
    if n <= 1:
        return m.group()
    w = w[:-1]
    if n == 2:
        return '{} bu{}'.format(n, w)
    elif n <= 9:
        return '{} {}zo'.format(n, w)
    else:
        return '{} ga{}ga'.format(n, w)


def sursurungal(txt):
    return re.sub('(\d+) (\w+)', s, txt)
