def vert_mirror(strng):
    return "\n".join(w[::-1] for w in strng.split("\n"))


def hor_mirror(strng):
    return "\n".join(strng.split("\n")[::-1])


def oper(fct, strng):
    return fct(strng)
