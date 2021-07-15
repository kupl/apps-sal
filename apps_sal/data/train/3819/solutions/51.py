def smash(arr):
    emptystring = ''
    for eachword in arr:
        emptystring = emptystring + eachword + ' '
    emptystring = emptystring.rstrip()
    return emptystring
