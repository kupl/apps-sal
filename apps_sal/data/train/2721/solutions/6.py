def pyramid(n):
    return ''.join(('{}/{}\\\n'.format(' ' * (n - i - 1), '_ '[i < n - 1] * i * 2) for i in range(n)))
