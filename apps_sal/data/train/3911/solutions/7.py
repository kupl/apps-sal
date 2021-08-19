def howmuch(m, n):
    arr = []
    for i in range(min(m, n), max(m, n) + 1):
        if ((i - 2) / 7).is_integer() and ((i - 1) / 9).is_integer():
            x = int((i - 2) / 7)
            y = int((i - 1) / 9)
            arr.append(['M: {0}'.format(i), 'B: {0}'.format(x), 'C: {0}'.format(y)])
    return arr
