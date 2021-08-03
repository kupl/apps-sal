def vert_mirror(strng):
    return "\n".join([strng.split('\n')[i][::-1] for i in range(len(strng.split('\n')))])


def hor_mirror(strng):
    return "\n".join(strng.split('\n')[::-1])


def oper(fct, s):
    return fct(s)
