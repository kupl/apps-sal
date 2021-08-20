def my_crib(n):
    w = n * 2
    return '\n'.join([('/' + ' ' * (i * 2) + '\\').center(w + 2) for i in range(n)] + ['/' + '_' * w + '\\'] + ['|' + ' ' * w + '|'] * (n - 1) + ['|' + '_' * w + '|'])
