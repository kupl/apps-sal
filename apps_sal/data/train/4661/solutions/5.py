def pattern(n):
    p = ' ' * (n - 1) + ''.join((str(x % 10) for x in range(1, n + 1))) + ' ' * (n - 1)
    return '\n'.join((p[x:x + 2 * n - 1] for x in range(n)))
