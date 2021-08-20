def count_sheep(n):
    str = ''
    for i in range(n):
        str = str + '{} sheep...'.format(i + 1)
    return str
