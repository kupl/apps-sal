def pattern(n, m=1, *args):
    if n < 1:
        return ''
    m = max(m, 1)
    r = ['{0}{1}{2}{1}{0}'.format(' ' * (i - 1), i % 10, ' ' * ((n - i) * 2 - 1)) for i in range(1, n)]
    r = r + ['{0}{1}{0}'.format(' ' * (n - 1), n % 10)] + r[::-1]
    return '\n'.join(r + r[1:] * (m - 1))
