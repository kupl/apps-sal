def vert_mirror(strng):
    return "\n".join([e[::-1] for e in strng.split()])


def hor_mirror(strng):
    return "\n".join([e for e in strng.split()[::-1]])


def oper(fct, s):
    return fct(s)
