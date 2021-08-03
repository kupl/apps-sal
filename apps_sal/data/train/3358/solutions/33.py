def correct(string):
    inpstr = string
    oplst = []
    for c in inpstr:
        if c.isnumeric():
            if int(c) == 0:
                oplst.append('O')
            elif int(c) == 5:
                oplst.append('S')
            elif int(c) == 1:
                oplst.append('I')
        else:
            oplst.append(c)

    return ''.join(oplst)
