def count_sheep(n):
    x = 1
    list = []
    while x <= n:
        sheep = '{} sheep...'.format(x)
        list.append(sheep)
        x += 1
    return ''.join(list)
