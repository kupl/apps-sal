def multi_table(number):
    res = ''
    for i in range(10):
        res += f'{i + 1} * {number} = {(i + 1) * number}\n'
    return res[:-1]
