def multi_table(number):
    result = ''

    for i in range(1, 10 + 1):
        result += '{} * {} = {}\n'.format(i, number, i * number)

    return result[:-1]
