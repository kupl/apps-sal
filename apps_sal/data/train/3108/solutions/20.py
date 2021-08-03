def multi_table(number):
    s = ''
    for i in range(1, 10):
        s = s + str(i) + ' * ' + str(number) + ' = ' + str(i * number) + '\n'
    return s + '10' + ' * ' + str(number) + ' = ' + str(10 * number)
