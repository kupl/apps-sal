def pattern(n):
    emptystring = ''
    for i in range(1, n + 1):
        if i == n:
            emptystring = emptystring + '{}'.format(str(i) * i)
        else:
            emptystring = emptystring + '{}'.format(str(i) * i) + '\n'
    return emptystring
