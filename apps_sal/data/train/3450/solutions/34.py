def array(string):
    a = list(string.split(','))
    if len(a) <= 2:
        return None
    else:
        return ' '.join(a[1:-1])
