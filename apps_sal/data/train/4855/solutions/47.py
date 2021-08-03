def vert_mirror(strng):
    return '\n'.join(w[::-1] for w in strng.split())


def hor_mirror(strng):
    return '\n'.join(strng.split()[::-1])


def oper(fct, s):
    return fct(s)
