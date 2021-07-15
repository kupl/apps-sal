def vert_mirror(strng):
    return "\n".join([x[::-1] for x in strng.split("\n")])
def hor_mirror(strng):
    return "\n".join(strng.split("\n")[::-1])
def oper(fct, s):
    return fct(s)

