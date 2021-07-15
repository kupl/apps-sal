def vert_mirror(strng):
    lst = strng.split()[::-1]
    return "\n".join(lst)[::-1]


def hor_mirror(strng):
    lst = strng.split()[::-1]
    return "\n".join(lst)


def oper(fct, s):
    return fct(s)
