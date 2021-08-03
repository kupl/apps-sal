from itertools import chain


def pattern(n):
    xs = ''.join(str(i) for i in range(1, n + 1))
    return '\n'.join(''.join(str(j) for j in chain(range(i, n + 1), range(1, i))) for i in range(1, n + 1))
