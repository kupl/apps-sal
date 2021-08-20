def vert_mirror(strng):
    a = strng.split('\n')
    b = [i[::-1] for i in a]
    return '\n'.join(b)


def hor_mirror(strng):
    a = strng.split('\n')
    b = a[::-1]
    return '\n'.join(b)


def oper(fct, s):
    return fct(s)
