def array(string):
    x = string.replace(' ', '').split(',')
    return ' '.join(x[1:-1]) if len(x) > 2 else None
