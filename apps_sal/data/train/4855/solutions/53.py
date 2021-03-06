def vert_mirror(strng):
    return '\n'.join((cs[::-1] for cs in strng.split('\n')))


def hor_mirror(strng):
    return '\n'.join(strng.split('\n')[::-1])


def oper(fct, s):
    return vert_mirror(s) if fct == vert_mirror else hor_mirror(s)
