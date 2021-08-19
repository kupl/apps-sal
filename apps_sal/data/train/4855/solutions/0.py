def vert_mirror(s):
    return '\n'.join((line[::-1] for line in s.split('\n')))


def hor_mirror(s):
    return '\n'.join(s.split('\n')[::-1])


def oper(fct, s):
    return fct(s)
