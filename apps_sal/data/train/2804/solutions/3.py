from itertools import chain, cycle, islice, repeat


def custom_christmas_tree(chars, n):
    it = cycle(chars)
    leaves = (' '.join(islice(it, i)).center(2 * n - 1).rstrip() for i in range(1, n + 1))
    trunk = repeat('|'.rjust(n), n // 3)
    return '\n'.join(chain(leaves, trunk))
