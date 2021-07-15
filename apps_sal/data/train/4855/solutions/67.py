def vert_mirror(strng):
    s = strng.split("\n")
    l = list()
    for i in s:
        l.append(i[::-1])
    return "\n".join(str(i) for i in l)
def hor_mirror(strng):
    s = strng.split("\n")
    return "\n".join(str(i) for i in s[::-1])
def oper(fct, s):
    return fct(s)
