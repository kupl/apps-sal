def vert_mirror(string):
    return '\n'.join((s[::-1] for s in string.split('\n')))


def hor_mirror(string):
    return '\n'.join(string.split('\n')[::-1])


def oper(fct, s):
    return fct(s)
