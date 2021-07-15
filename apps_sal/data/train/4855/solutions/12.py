def vert_mirror(str_):
    return "\n".join(word[::-1] for word in str_.split("\n"))

def hor_mirror(str_):
    return "\n".join(str_.split("\n")[::-1])

def oper(fct, str_):
    return fct(str_)
