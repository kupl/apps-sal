def array(string):
    res = ' '.join(string.split(',')[1:-1])
    return res if res else None
