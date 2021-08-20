def multi_table(number):
    return '\n'.join(('{} * {} = {}'.format(x, number, x * number) for x in range(1, 11)))
