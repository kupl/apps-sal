from itertools import chain


def stairs(n):
    if n < 1:
        return ' '
    w = 4 * n - 1
    xs = [str(i % 10) for i in chain(range(1, n + 1), range(n, 0, -1))]
    return '\n'.join((' '.join(xs[:i] + xs[-i:]).rjust(w) for i in range(1, n + 1)))
