def expanded_form1(num):
    a = len(str(num))
    b = []
    for (i, j) in enumerate(str(num)):
        if j != '0':
            b.append(j + '0' * (a - i - 1))
    return ' + '.join(b)


def expanded_form(num):
    a = str(num).index('.')
    m = int(str(num)[:a])
    n = '0' + str(num)[a + 1:]
    b = []
    for (i, j) in enumerate(n[1:]):
        if j != '0':
            b.append(j + '/1' + '0' * (i + 1))
    b = ' + '.join(b)
    if len(expanded_form1(m)) > 0:
        return expanded_form1(m) + ' + ' + b
    else:
        return b
