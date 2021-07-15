def stringy(size):
    c, l = '1', []
    for i in range(size):
        if c=='1':
            l.append(c)
            c = '0'
        elif c=='0':
            l.append(c)
            c = '1'
    return ''.join(l)
