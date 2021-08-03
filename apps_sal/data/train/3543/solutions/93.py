def increment_string(s):
    l = []
    for i in s[::-1]:
        if i.isdigit():
            l.append(int(i))
        else:
            break
    l.reverse()
    if len(l) != 0:
        p = ''.join(map(str, l))
        q = p.lstrip('0')
        if len(q) > 0:
            r = int(q) + 1
            s = s[:len(s) - len(l)] + str(r).zfill(len(l))
        else:
            s = s[:len(s) - len(l)] + '1'.zfill(len(l))
    else:
        s = s + '1'
    return s
