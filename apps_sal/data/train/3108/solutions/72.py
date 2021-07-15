def multi_table(number):
    table = ''
    for i in range(1, 11):
        table += f'{i} * {number} = {i * number}'
        if i < 10:
            table += '\n'
    return table
