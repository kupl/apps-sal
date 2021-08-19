def vert_mirror(strng):
    return [x[::-1] for x in strng]


def hor_mirror(strng):
    return strng[::-1]


def oper(fct, s):
    strng = s.split('\n')
    return '\n'.join(fct(strng))
