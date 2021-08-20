def a(n):
    if n < 4:
        return ''
    if n % 2:
        n -= 1
    lines = ('A' if i == 0 else ' '.join('A' * (i + 1)) if i == n // 2 else 'A' + ' ' * (2 * i - 1) + 'A' for i in range(n))
    width = 2 * n - 1
    return '\n'.join((line.center(width) for line in lines))
