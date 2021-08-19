from re import sub


def reversi_row(moves):
    current = '.' * 8
    for (i, x) in enumerate(moves):
        (c1, c2) = 'Ox' if i & 1 else 'xO'
        left = sub('(?<={}){}+$'.format(c1, c2), lambda r: c1 * len(r.group()), current[:x])
        right = sub('^{}+(?={})'.format(c2, c1), lambda r: c1 * len(r.group()), current[x + 1:])
        current = left + c1 + right
    return current.replace('x', '*')
