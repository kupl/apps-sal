def array(string):
    res = ' '.join(string.split(',')[1:-1])
    if not res:
        return None
    return res
