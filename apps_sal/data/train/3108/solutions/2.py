def multi_table(number):
    return '\n'.join(['{1} * {0} = {2}'.format(number, i, i * number) for i in range(1, 11)])
