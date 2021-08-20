def multi_table(number):
    return '\n'.join(('{} * {} = {}'.format(c, number, c * number) for c in range(1, 11)))
