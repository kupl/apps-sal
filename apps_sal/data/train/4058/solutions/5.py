def pattern(n):
    up = ['{0}{1}{0}'.format(x % 10, ' ' * (2 * (n - x) - 1)).center(2 * n - 1) for x in range(1, n)]
    return '\n'.join(up + [str(n % 10).center(2 * n - 1)] + up[::-1]) if n > 0 else ''
