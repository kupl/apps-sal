def count_sheep(n):
    sheep = ''
    for i in range(n):
        sheep += '{} sheep...'.format(i + 1)
    return sheep
