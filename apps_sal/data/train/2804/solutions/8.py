from itertools import cycle


def custom_christmas_tree(chars, n):
    (l, s) = (cycle(chars), lambda i=0: ' ' * (n - 1 - i))
    return '\n'.join([s(i) + ' '.join((next(l) for _ in range(i + 1))) for i in range(n)] + [f'{s()}|' for _ in range(n // 3)])
