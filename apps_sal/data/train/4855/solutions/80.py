def vert_mirror(s):
    return "\n".join(["".join([line[i] for i in range(len(line) - 1, -1, -1)]) for line in s.splitlines()])


def hor_mirror(s):
    return "\n".join([s.splitlines()[i] for i in range(len(s.splitlines()) - 1, -1, -1)])


def oper(fct, s):
    return fct(s)
