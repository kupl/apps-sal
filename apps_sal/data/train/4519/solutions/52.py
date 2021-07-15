def max_number(n):
    x = str(n)
    x = list(x)
    emptylist = sorted(list([int(eachletter) for eachletter in x]))
    emptylist.reverse()
    emptystring = ''
    for eachnumber in emptylist:
        emptystring = emptystring + str(eachnumber)
    return int(emptystring)
