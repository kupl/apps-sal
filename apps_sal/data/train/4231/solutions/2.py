def a(n):
    n -= n % 2
    if n < 4:
        return ''
    return '\n'.join('{0}{1}{0}'.format('A' * (i % (n // 2) != 0),
                                        ' ' * (i * 2 - 1) if i % (n // 2) else ' '.join(['A'] * (i + 1))
                                        ).center(2 * n - 1) for i in range(n))
