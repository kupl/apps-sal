def countzero(string):
    counter = 0
    for x in string:
        if x in 'abdegopq069DOPQR':
            counter += 1
        elif x in '%&B8':
            counter += 2
        else:
            pass
    return counter + string.count('()')
