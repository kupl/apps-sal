def vert_mirror(string):
    return "\n".join(row[::-1] for row in string.split("\n"))


def hor_mirror(string):
    return "\n".join(string.split("\n")[::-1])


def oper(fct, string):
    return fct(string)
