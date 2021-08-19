def multi_table(number):
    counter = 1
    table = ''
    while counter < 11:
        table += str(counter) + ' * ' + str(number) + ' = ' + str(number * counter) + '\n'
        counter += 1
    return table[:-1]
