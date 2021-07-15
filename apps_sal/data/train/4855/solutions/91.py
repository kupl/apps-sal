def vert_mirror(s):
    return "\n".join([w[::-1] for w in s.split("\n")])
def hor_mirror(s):
    return "\n".join([w for w in s.split("\n")][::-1])
def oper(fct, s):
    return fct(s)
