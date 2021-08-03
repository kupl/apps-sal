def my_crib(n):
    l, res = n + 1 << 1, []
    res.extend('/' + ' ' * (2 * i) + '\\' for i in range(n))
    res.append('/' + '_' * (2 * n) + '\\')
    res.extend('|' + ' ' * (l - 2) + '|' for _ in range(n - 1))
    res.append('|' + '_' * (l - 2) + '|')
    return '\n'.join(s.center(l) for s in res)
