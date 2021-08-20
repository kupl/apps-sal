def my_crib(n):
    temp = []
    temp.append(' ' * (2 * n) + '_' * (2 * n + 1) + ' ' * (2 * n))
    for i in range(2 * n):
        strr = '\n' + (2 * n - i - 1) * ' ' + '/' + (2 * n + 1 + 2 * i) * '_' + '\\'
        if i != 2 * n and i != 2 * n - 1:
            strr += ' ' * (2 * n - i - 1)
        temp.append(strr)
    strr2 = '\n|' + (n * 6 - 1) * ' ' + '|'
    temp.append((n - 1) * strr2)
    strr3 = '\n|' + 2 * n * ' ' + (2 * n - 1) * '_' + 2 * n * ' ' + '|'
    temp.append(strr3)
    strr4 = '\n|' + (2 * n - 1) * ' ' + '|' + (2 * n - 1) * ' ' + '|' + (2 * n - 1) * ' ' + '|'
    temp.append((n - 1) * strr4)
    temp.append('\n|')
    strr5 = (2 * n - 1) * '_' + '|'
    temp.append(3 * strr5)
    temp2 = ''.join(temp)
    return temp2
