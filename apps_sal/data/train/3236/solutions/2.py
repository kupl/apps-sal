def my_crib(n):
    n *= 2
    mansion = ['{}{}{}'.format(' ' * n, '_' * (n + 1), ' ' * n)]
    mansion.extend(('{0}/{1}\\{0}'.format(' ' * (n - i - 1), '_' * (n + 1 + 2 * i)) for i in range(n)))
    mansion.extend(('|{}|'.format(' ' * (3 * n - 1)) for i in range(n // 2 - 1)))
    mansion.append('|{0}{1}{0}|'.format(' ' * n, '_' * (n - 1)))
    mansion.extend(('|{0}|{0}|{0}|'.format(' ' * (n - 1)) for i in range(n // 2 - 1)))
    mansion.append('|{0}|{0}|{0}|'.format('_' * (n - 1)))
    return '\n'.join(mansion)
