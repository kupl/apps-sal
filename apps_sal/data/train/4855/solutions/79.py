def vert_mirror(strng):
    return '\n'.join((elem[::-1] for elem in strng.split('\n')))


def hor_mirror(strng):
    return '\n'.join(strng.split('\n')[::-1])


def oper(fct, s):
    return fct(s)
