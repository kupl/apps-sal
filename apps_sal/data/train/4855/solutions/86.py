def vert_mirror(strng):
    return '\n'.join([s[::-1] for s in strng.split('\n')])


def hor_mirror(strng):
    return '\n'.join([s for s in strng.split('\n')[::-1]])


def oper(fct, s):
    return fct(s)
