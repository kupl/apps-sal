def array(string):
    l = string.split(',')
    return None if not len(l) >= 3 else ' '.join(l[1:-1])
