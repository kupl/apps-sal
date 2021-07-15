def array(s):
    a = s.split(',')
    if len(a)>2:
        return ' '.join(a[1:-1])
