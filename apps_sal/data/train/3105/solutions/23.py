def count_sheep(n):
    return ''.join(['{} sheep...'.format(x) for x in list(range(n + 1))[1::]])
