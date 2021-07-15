def multi_table(number):
    msg = ''
    for x in range(1,11):
        msg += str(x) + ' * ' + str(number) + ' = ' + str(x*number) + '\n'
    return msg[0:-1]
