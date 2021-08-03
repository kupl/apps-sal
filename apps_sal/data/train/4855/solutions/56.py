def vert_mirror(str):
    return '\n'.join([i[::-1] for i in str.split('\n')])


def hor_mirror(str):
    return '\n'.join(str.split('\n')[::-1])


def oper(fct, s):
    return fct(s)
