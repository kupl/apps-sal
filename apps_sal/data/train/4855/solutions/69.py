def vert_mirror(strng):
    strng = strng.split("\n")
    return "\n".join(s[::-1] for s in strng)


def hor_mirror(strng):
    strng = strng.split("\n")
    return "\n".join(strng[::-1])


def oper(fct, s):
    return fct(s)
