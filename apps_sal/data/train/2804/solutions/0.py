def custom_christmas_tree(chars, n):
    from itertools import cycle
    it = cycle(chars)
    tree = [' '.join(next(it) for j in range(i)).center(2 * n).rstrip() for i in range(1, n + 1)]
    tree.extend('|'.center(2 * n).rstrip() for _ in range(n // 3))
    return '\n'.join(tree)
