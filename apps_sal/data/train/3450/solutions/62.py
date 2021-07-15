def array(string):
    x = string.split(',')
    r = None
    if len(x) > 2:
        r = ' '.join(x[1:-1])
    return r
