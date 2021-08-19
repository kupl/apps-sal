def array(string):
    v = string.split(',')
    if len(v) > 2:
        v.pop()
        v.pop(0)
        return ' '.join(v)
    else:
        return None
