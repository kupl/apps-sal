def two_sort(array):
    array = sorted(array)
    emptystring = ''
    for eachletter in array[0]:
        emptystring = emptystring + eachletter + ' '
    emptystring = emptystring.rstrip()
    emptystring = emptystring.split()
    emptystring = '***'.join(emptystring)
    return emptystring
