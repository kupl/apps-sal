def multi_table(number):
    res = ''
    for i in range(1, 11):
        res += '{} * {} = {}\n'.format(i, number, i * number)
    return res[:-1]
