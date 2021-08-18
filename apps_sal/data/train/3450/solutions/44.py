def array(string):

    l = string.replace(' ', '').split(',')

    return ' '.join(l[1:-1]) if len(l) >= 3 else None
