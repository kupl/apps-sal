def friend_find(line):
    s = ''.join([[c[0],'y'][c not in ['red','green','blue']] for c in line])
    r = ''
    c = 0
    for i in s:
        if len(r) < 3:
            r += i
        else:
            r = (r+i)[1:]
        if [r.count('r'),r.count('b')] == [1,2]:
            c += 1
            n = ''
            for i in r:
                if i == 'r':
                    n += 'x'
                else:
                    n += i
            r = n[:]
    return c
