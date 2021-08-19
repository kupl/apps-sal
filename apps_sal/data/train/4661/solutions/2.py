def pattern(n):
    s = ''.join((str(i % 10) for i in range(1, n + 1)))
    return '\n'.join((' ' * i + s + ' ' * (n - i - 1) for i in range(n - 1, -1, -1)))
