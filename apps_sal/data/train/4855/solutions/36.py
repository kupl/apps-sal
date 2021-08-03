def vert_mirror(strng):
    v_mirror = []
    for row in strng.split("\n"):
        v_mirror.append(row[::-1])
    return "\n".join(v_mirror)


def hor_mirror(strng):
    return "\n".join(list(reversed(strng.split("\n"))))


def oper(fct, s):
    if fct == vert_mirror:
        return vert_mirror(s)
    else:
        return hor_mirror(s)
