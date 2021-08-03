def vert_mirror(strng):
    l = strng.split('\n')
    p = []
    for i in l:
        p.append(i[::-1])
    return '\n'.join(p)


def hor_mirror(strng):
    l = list(reversed(strng.split('\n')))
    return '\n'.join(l)


def oper(fct, s):
    return fct(s)
