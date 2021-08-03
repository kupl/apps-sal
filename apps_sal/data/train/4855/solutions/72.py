def vert_mirror(strng):
    return '\n'.join([a[::-1] for a in strng.split('\n')])


def hor_mirror(strng):
    return '\n'.join(reversed(strng.split('\n')))


def oper(fct, s):
    return fct(s)
