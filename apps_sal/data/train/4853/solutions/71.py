def double_char(s):
    l = list(s)
    r = []
    for i in range(len(l)):
        r.append(l[i] + l[i])
    return ''.join(r)
