def vert_mirror(strng):
    return '\n'.join([text[::-1] for text in strng.split('\n')])


def hor_mirror(strng):
    return '\n'.join(strng.split('\n')[::-1])


def oper(fct, s):
    return vert_mirror(s) if fct is vert_mirror else hor_mirror(s)
