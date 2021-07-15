def dot(n, m):
    sep = '+---' * n + '+'
    dot = '| o ' * n + '|'
    return '\n'.join([sep, dot] * m + [sep])
