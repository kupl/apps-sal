def array(s):
    m = s.split(',')
    if len(m) <= 2:
        return None
    return ' '.join(m[1:-1])
