def pattern(n):
    l = 2 * n - 1
    base = ''.join(str(x % 10) for x in range(1, n + 1))
    return '\n'.join((base + ' ' * x).rjust(l) for x in range(n))
