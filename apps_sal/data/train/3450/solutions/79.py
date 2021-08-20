def array(string):
    s = string.split(',')
    return None if len(s) < 3 else ' '.join((x for x in s[1:-1]))
