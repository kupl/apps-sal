def multi_table(n):
    return '\n'.join(['{0} * {1} = {2}'.format(i, n, i * n) for i in range(1, 11)])
