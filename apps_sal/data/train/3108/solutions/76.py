def multi_table(number):
    n = str(number)
    i = 1
    string = ''
    while i <= 10:
        ans = i * number
        string = string + str(i) + ' * ' + n + ' = ' + str(ans) + '\n'
        i = i + 1
    return string[:len(string) - 1]
