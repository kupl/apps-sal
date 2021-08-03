def vert_mirror(strng):
    return '\n'.join(''.join(reversed(line)) for line in strng.split('\n'))


def hor_mirror(strng):
    return '\n'.join(reversed(strng.split('\n')))


def oper(fct, s):
    return fct(s)
