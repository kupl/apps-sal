def array(string):
    newstring = string.strip().split(',')
    l = newstring[1:-1]
    s = ' '.join(l)
    if len(s) == 0:
        print(None)
    else:
        return s
