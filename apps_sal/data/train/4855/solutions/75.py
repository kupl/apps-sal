def vert_mirror(strng):
    p = []
    s = strng.split("\n")
    for i in s:
        p.append(i[::-1])
    return "\n".join(p)


def hor_mirror(strng):
    s = strng.split("\n")
    p = s[::-1]
    return "\n".join(p)


def oper(fct, s):
    return fct(s)
