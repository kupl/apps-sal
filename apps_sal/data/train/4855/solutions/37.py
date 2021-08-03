def vert_mirror(strng):
    s = strng.split('\n')
    return '\n'.join([x[::-1] for x in s])


def hor_mirror(strng):
    s = strng.split('\n')
    return '\n'.join(s[::-1])


def oper(fct, s):
    return fct(s)
