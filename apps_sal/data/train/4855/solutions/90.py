def vert_mirror(strng):
    a = strng.split("\n")
    vert_m = ''

    for word in a:
        vert_m +=word[::-1] +"\n"

    return vert_m.strip("\n")


def hor_mirror(strng):
    a = strng.split("\n")
    a.reverse()
    hor_m = ''

    for word in a:
        hor_m += word + "\n"

    return hor_m.strip("\n")


def oper(fct, s):
    return fct(s)
