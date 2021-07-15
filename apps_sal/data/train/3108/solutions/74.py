def multi_table(number):
    table = ""
    for x in range(1,11):
        table += str(x) + ' * ' + str(number) + ' = ' + str(x * number) + '\n'
    return table[:-1]
