def multi_table(number):
    emptystring = ''
    for eachnumber in range(1, 11):
        if eachnumber == 10:
            emptystring = emptystring + '{} * {} = {}'.format(eachnumber, number, eachnumber * number)
        else:
            emptystring = emptystring + '{} * {} = {}\n'.format(eachnumber, number, eachnumber * number)
    return emptystring
