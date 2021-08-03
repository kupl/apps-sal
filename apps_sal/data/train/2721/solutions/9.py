def pyramid(n):
    return '\n'.join([' ' * (n - i - 1) + '/' + ' ' * (2 * i) + '\\' for i in range(n - 1)] + ['/' + '_' * (2 * n - 2) + '\\']) + '\n'
