def vert_mirror(strng):
    k = [i[::-1] for i in strng.split('\n')]
    return '\n'.join(k)


def hor_mirror(strng):
    l = strng.split('\n')[::-1]
    return '\n'.join(l)


def oper(fct, s):
    return fct(s)
