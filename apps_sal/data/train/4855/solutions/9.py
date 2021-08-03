def vert_mirror(strng):
    return [x[::-1] for x in strng.split("\n")]


def hor_mirror(strng):
    return strng.split("\n")[::-1]


def oper(fct, s):
    return '\n'.join(list(map(fct, [s]))[0])
