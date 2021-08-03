def count_place(s):
    l = list(s)
    l.reverse()
    c = 0
    for i, each in enumerate(l):
        if each == 'o' or each == 'O':
            continue
        if each == 'k':
            c += 2**i
    return c


def okkOokOo(s):
    ret = []
    for each in s.split('? '):
        new_s = each.replace(', ', '')
        if new_s[-1] == '!':
            new_s = new_s[:-1]
        location = count_place(new_s)
        ret.append(chr(location))
    return ''.join(ret)
