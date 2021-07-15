def multi_table(number):
    s = ''
    for i in range(1,11):
        if i > 1:
            s += '\n'
        s += str(i) + ' * ' + str(number) + ' = ' + str(i*number)
    return s
