def my_crib(n):
    r, ws, wu = ['_' * (2 * n + 1)], ' ' * (2 * n - 1), '_' * (2 * n - 1)
    r += ['/' + '_' * (2 * (n + i) + 1) + '\\' for i in range(2 * n)]
    r += ['|' + ws + ' ' + ws + ' ' + ws + '|' for i in range(n - 1)]
    r += ['|' + ws + ' ' + wu + ' ' + ws + '|']
    r += ['|' + ws + '|' + ws + '|' + ws + '|' for i in range(n - 1)]
    r += ['|' + wu + '|' + wu + '|' + wu + '|']
    return '\n'.join(l.center(n * 6 + 1) for l in r)
