def vert_mirror(strng: str):
    return "\n".join(el[::-1] for el in strng.split())


def hor_mirror(strng: str):
    return "\n".join(reversed(strng.split()))


def oper(fct, s):
    return fct(s)
