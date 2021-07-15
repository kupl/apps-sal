def array(string):
    x = string.split(',')
    y = x[1:-1]
    return None if len(x) < 3 else ' '.join(y)
