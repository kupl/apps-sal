def vert_mirror(s):
    return '\n'.join((r[::-1] for r in s.split('\n')))


def hor_mirror(s):
    return '\n'.join(s.split('\n')[::-1])


def oper(f, s):
    return f(s)
