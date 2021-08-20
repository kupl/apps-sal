def array(string):
    rez = string.split(',')
    if len(rez) <= 2:
        return None
    s = ''
    for x in range(1, len(rez) - 1):
        s = s + rez[x] + ' '
    return s[:-1]
