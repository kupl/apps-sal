def christmas_tree(n):
    return '\r\n'.join([('*' * (j - p)).center(n // 3 * 2 + 3, ' ').rstrip() for (o, i) in enumerate(range(1, n // 3 * 3, 3)) for (p, j) in enumerate(range(i - o, i - o + 9, 3))] + ['###'.center(n // 3 * 2 + 3).rstrip()] if n > 2 else '')
