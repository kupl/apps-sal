def vert_mirror(strng):
    return '\n'.join((s[::-1] for s in strng.split('\n')))


def hor_mirror(strng):
    return '\n'.join(reversed(strng.split('\n')))


def oper(fct, s):
    return fct(s)
