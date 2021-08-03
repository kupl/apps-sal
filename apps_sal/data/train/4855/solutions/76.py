def vert_mirror(strng):
    return '\n'.join(list(map(lambda x: x[::-1], strng.split('\n'))))


def hor_mirror(strng):
    return '\n'.join(list(map(lambda x: x[::-1], strng[::-1].split('\n'))))


def oper(fct, s):
    return fct(s)
