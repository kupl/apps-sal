def multi_table(number):
    string = ''
    i = 0
    for multiply in range(1, 10):
        i += 1
        string = string + f'{multiply} * {number} = {multiply * number}\n'
    else:
        string = string + f'{10} * {number} = {10 * number}'
    return string
