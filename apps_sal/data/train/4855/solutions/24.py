def vert_mirror(strng):
    return '\n'.join((i[::-1] for i in strng))


def hor_mirror(strng):
    return '\n'.join((i for i in strng[::-1]))


def oper(fct, s):
    return fct(s.split('\n'))
