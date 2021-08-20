def count_sheep(n):
    hold = ''
    for i in range(n):
        hold += '{} sheep...'.format(i + 1)
    return hold
