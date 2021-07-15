def array(string):
    if len(string.split(',')) > 2:
        a = string.split(',')[1:-1]
        k = ''
        for c in a:
            k = k + c + ' '
        return k[:-1]
    else:
        return None
