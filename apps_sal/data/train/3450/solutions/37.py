def array(string):
    l = string.split(',')
    if len(l) < 3:
        return
    return ' '.join(x.strip() for x in l[1:-1])
