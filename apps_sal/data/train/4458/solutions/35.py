def time_correct(t):
    if t == '':
        return ''
    elif t:
        l = t.split(':')
        if len(l) == 3 and all(i.isdigit() for i in l):
            a, b = divmod(int(l[2]), 60)
            l[2] = str(b).zfill(2)
            c, d = divmod(int(l[1]) + a, 60)
            l[1] = str(d).zfill(2)
            l[0] = str((int(l[0]) + c) % 24).zfill(2)
            return ':'.join(l)
