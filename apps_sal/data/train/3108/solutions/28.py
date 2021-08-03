def multi_table(number):
    s = ''
    for i in range(1, 11):
        result = number * i
        r = (str((str(i) + ' * ' + str(number) + ' = ' + str(result))))
        if i in range(1, 10):
            s += r + '\n'
        else:
            s += r
    return s
