def array(string):
    m = string.split(',')
    if len(m) > 2:
        return ' '.join(m[1:-1])
    else:
        return None
