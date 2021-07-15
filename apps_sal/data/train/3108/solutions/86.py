def multi_table(number):
    table = ''
    for n in range(1, 11):
        table += '{0} * {1} = {2}'.format(n, number, n*number)
        if n < 10:
            table += '\n'
    return table
