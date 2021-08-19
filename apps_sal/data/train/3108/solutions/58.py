def multi_table(number):
    return ''.join((f'{i} * {number} = {i * number}\n' for i in range(1, 11)))[0:-1]
