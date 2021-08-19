from itertools import cycle, islice


def f(n):
    it = cycle('1234567890')
    xs = ''.join(islice(it, 0, n - 1))
    return xs + next(it) + xs[::-1]


def pattern(n):
    m = n * 2 - 1
    return '\n'.join(('{:^{}}'.format(f(i), m) for i in range(1, n + 1)))
