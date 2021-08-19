def multi_table(number):
    res = ''
    for i in range(1, 11):
        res += str(i) + ' * ' + str(number) + ' = ' + str(i * number)
        if i != 10:
            res += '\n'
    return res
