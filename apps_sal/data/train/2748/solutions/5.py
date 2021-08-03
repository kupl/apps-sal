def namelist(names):
    l = []
    if len(names) == 0:
        return ''
    else:
        for name in names:
            l.append(''.join(list(name.values())))
        str = ', '
        if len(l) == 1:
            return l[0]
        else:
            return str.join(l[:-1]) + ' & ' + l[-1]
