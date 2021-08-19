def multi_table(number):
    c = ''
    for i in range(1, 11):
        c = c + '{} * {} = {}'.format(i, number, number * i) + '\n'
    return c.rstrip('\n')
