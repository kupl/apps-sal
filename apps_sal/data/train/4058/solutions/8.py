def get_r(y):
    return str((y + 1) % 10)


def row(n, i):
    return ' ' * i + get_r(i) + ' ' * max(0, 2 * n - 3 - i * 2) + (get_r(i) if i != n - 1 else '') + ' ' * i


def pattern(n):
    if n < 1:
        return ''
    top = [row(n, x) for x in range(n - 1)]
    return '\n'.join(top + [row(n, n - 1)] + list(reversed(top)))
